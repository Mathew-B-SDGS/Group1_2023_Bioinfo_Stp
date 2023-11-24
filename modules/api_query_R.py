import requests
import sys


class RCodeToBedFile():
    """Takes a GMS R code (e.g. R169), a reference genome
    (GRCh38/37) and returns the list of genes and creates a bedfile
    containing Mane Select transcript coordinates or padded exon
    coordinates.
    :test_code:
    """

    def __init__(self, test_code, GRCh38=True,
                 padded_exons=True):
        if GRCh38:
            self.ref_genome = 'GRCh38'
        else:
            self.ref_genome = 'GRCh37'
        self.test_code = test_code
        self.padded_exons = padded_exons

    def get_panel_for_genomic_test(self):
        """Queries the panel app API to retrieve genes within the panel
        associated with R code
        """
        panel_api_url = "https://panelapp.genomicsengland.co.uk/api/v1/panels/"
        panel_endpoint = panel_api_url + self.test_code + "/"
        response = requests.get(panel_endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve panels querying the PanelApp API using"
                  f" {self.test_code}")
            sys.exit(1)

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
        gene_list = self.extract_genes_hgnc()
        chrom_start_end = []
        all_gene_coords = []
        transcript_coords = []
        for gene in gene_list:
            vv_url = (f"https://rest.variantvalidator.org/VariantValidator/"
                      f"tools/gene2transcripts_v2/{gene}/mane/refseq/"
                      f"{self.ref_genome}")
            response = requests.get(vv_url)
            if response.status_code == 200:
                gene_info = response.json()
                mane_select = (list(gene_info[0]['transcripts'][0]
                                    ['genomic_spans'].keys()))[0]
                transcript_data = (gene_info[0]['transcripts'][0]
                                   ['genomic_spans'][mane_select])
                if self.padded_exons:
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
                    chrom_start_end.append(transcript_data['start_position'])
                    chrom_start_end.append(transcript_data['end_position'])
                    transcript_coords.append(chrom_start_end)
                all_gene_coords.append(transcript_coords)
            else:
                print("Failed to recieve response from Variant Validator API")
                sys.exit(1)
        return all_gene_coords

    def create_bed_file_iterable(self):
        """Creates a bedfile structure for front end creation of bedfile"""
        coords_for_bed = []
        for gene in self.get_coords_for_bed():
            for entity in gene:
                chrom, start, end = entity
                if self.padded_exons:
                    start = int(start) - 50
                    end = int(end) + 50
                line = str(chrom) + "\t" + str(start) + "\t" + str(end) + "\n"
                coords_for_bed.append(line)
        return coords_for_bed
