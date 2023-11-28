import requests
import sys


class RCodeToBedFile():
    """Takes a GMS R code (e.g. R169), a reference genome
    (GRCh38/37) and returns the list of genes and creates a bedfile
    containing Mane Select transcript coordinates or padded exon
    coordinates.
    :test_code:
    """

    def __init__(
        self,
        test_code,
        ref_genome,
        include_exon=True,
        padded=True
    ):

        self.ref_genome = ref_genome
        self.test_code = test_code.upper()
        if include_exon == 'Exon':
            self.include_exon = True
        else:
            self.include_exon = False
        if padded == 'True' or padded is True:
            self.padded = True
        else:
            self.padded = False

    def get_panel_for_genomic_test(self):
        """
        Queries the panel app API to retrieve genes within the panel
        associated with R code
        """
        try:
            panel_api_url = "https://panelapp.genomicsengland.co.uk/api/v1/panels/"
            panel_endpoint = panel_api_url + self.test_code + "/"
            response = requests.get(panel_endpoint)
            if response.status_code == 200:
                print(f"Successfully retrieved panel for {self.test_code}")
                return response.json()
            elif response.json()["detail"] == "Not found.":
                print(f"Panel for {self.test_code} not found")
                raise
            else:
                print(f"Failed to retrieve panels querying the PanelApp API using"
                      f" {self.test_code}")
        except Exception as e:
            print(self.__str__() + f"\nError: {str(e)}")
            raise

    def extract_genes_hgnc(self):
        """Extracts list of gene HGNC IDs from the PanelApp API query
        response from function above
        """
        gene_list = []
        gene_information = self.get_panel_for_genomic_test()
        for gene in gene_information["genes"]:
            gene_list.append(gene["gene_data"]["hgnc_id"])
        return gene_list

    def get_coords_for_bed(self):
        """Retrieves the coordinates for the bedfile, if padded_exons=True
        then exon coordinates will be retrieved else Mane Select transcript
        coordinates will be retrieved.
        """
        try:
            gene_list = self.extract_genes_hgnc()
            chrom_start_end = []
            all_gene_coords = []
            transcript_coords = []
            # Iterate through each gene in the list of genes queried from the
            # PanelApp API
            for gene in gene_list:
                vv_url = (f"https://rest.variantvalidator.org/VariantValidator/"
                          f"tools/gene2transcripts_v2/{gene}/mane/refseq/"
                          f"{self.ref_genome}")
                response = requests.get(vv_url)
                # If the response is successful, then retrieve the Mane Select
                if response.status_code == 200:
                    gene_info = response.json()
                    mane_select = (list(gene_info[0]['transcripts'][0]
                                        ['genomic_spans'].keys()))[0]
                    transcript_data = (gene_info[0]['transcripts'][0]
                                       ['genomic_spans'][mane_select])
                    # If padded_exons=True, then retrieve exon coordinates
                    # else retrieve Mane Select transcript coordinates
                    if self.include_exon is True:
                        for exon in transcript_data['exon_structure']:
                            chrom_start_end.append(gene_info[0]['transcripts'][0]
                                                   ['annotations']['chromosome'])
                            chrom_start_end.append(exon['genomic_start'])
                            chrom_start_end.append(exon['genomic_end'])
                            transcript_coords.append(chrom_start_end)
                            chrom_start_end = []
                    else:
                        chrom_start_end.append(gene_info[0]['transcripts'][0]
                                               ['annotations']['chromosome'])
                        chrom_start_end.append(
                            transcript_data['start_position'])
                        chrom_start_end.append(transcript_data['end_position'])
                        transcript_coords.append(chrom_start_end)
                    all_gene_coords.append(transcript_coords)
                else:
                    print("Failed to recieve response from Variant Validator API")
                    # sys.exit(1)
            return all_gene_coords
        except Exception as e:
            print(self.__str__() + f"\nError: {str(e)}")
            raise

    def pad_bed_files(self):
        """Creates a bedfile structure for front end creation of bedfile"""
        coords_for_bed = []
        try:
            for gene in self.get_coords_for_bed():
                for entity in gene:
                    # the entity is a looping list of 3 elements, so having a for to separate them into chrom, start and end
                    for i in range(0, len(entity), 3):
                        chrom, start, end = entity[i:i+3]
                    # Ensure start is non-negative
                        start = max(0, int(start) - 50)
                        end = int(end) + 50
                        coords_for_bed.append(
                            [str(chrom), int(start), int(end)])
            return coords_for_bed
        except Exception as e:
            print(self.__str__() + f"\nError: {str(e)}")
            raise

    def create_string_bed(self):
        """Creates a string representation of the bedfile"""
        try:
            if self.padded:
                input_bed_file = self.pad_bed_files()
            else:
                input_bed_file = self.get_coords_for_bed()[0]
            bed_file_string = ""
            for line in input_bed_file:
                bed_file_string += f"{line[0]}\t{line[1]}\t{line[2]}\n"
            return str(bed_file_string)
        except Exception as e:
            print(self.__str__() + f"\nError: {str(e)}")
            raise

    def __repr__(self):
        return f"RCodeToBedFile(test_code={self.test_code}, ref_genome={self.ref_genome}, padded_exons={self.include_exon})"

    def __str__(self):
        return f"RCodeToBedFile\nTest Code: {self.test_code}\nReference Genome: {self.ref_genome}\nPadded Exons: {self.include_exon}"

"""
test_code = 'R169'
ref_genome = 'GRCh38'

obj = RCodeToBedFile(test_code, ref_genome, padded=True, include_exon='Exons')
print(obj.pad_bed_files())

print(obj.get_coords_for_bed())
"""