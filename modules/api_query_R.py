import requests


class RcodeToBed():
    """
    Run code by calling class with R test code and desired reference genome
    """

    def __init__(self, test_code, ref_genome='GRCh38', padded_exons = True):
        self.test_code = test_code
        self.ref_genome = ref_genome
        self.padded_exons = padded_exons

    # Make a request to the API to retrieve all panels
    def get_panel_for_genomic_test(self):
        api_url = "https://panelapp.genomicsengland.co.uk/api/v1/panels/"
        endpoint = f"{api_url}"
        endpoint_2 = endpoint + self.test_code + '/'
        print(endpoint_2)
        response = requests.get(endpoint_2)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve panels")
            return None

    def extract_genes_hgnc(self):
        # extract gene name from json from above api query
        gene_list = []
        gene_information = self.get_panel_for_genomic_test()
        for gene in gene_information['genes']:
            gene_list.append(gene['gene_data']['hgnc_id'])
        return gene_list
    
    def get_coord_mane_select_trans(self):
        gene_list = self.extract_genes_hgnc()
        print(gene_list)
        chrom_start_end = []
        all_gene_coords = []
        for gene in gene_list:
            vv_url = f"https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts_v2/{gene}/mane/refseq/{self.ref_genome}"
            response = requests.get(vv_url)
            if response.status_code == 200:
                gene_info = response.json()
                mane_select = (list(gene_info[0]['transcripts'][0]['genomic_spans'].keys()))[0]
                transcript_data = gene_info[0]['transcripts'][0]['genomic_spans'][mane_select]
                transcript_coords = []
                if self.padded_exons:
                    for exon in transcript_data['exon_structure']:
                        chrom_start_end.append(gene_info[0]['transcripts'][0]['annotations']['chromosome'])
                        chrom_start_end.append(exon['genomic_start'])
                        chrom_start_end.append(exon['genomic_end'])
                        transcript_coords.append(chrom_start_end)
                        chrom_start_end = []
                else:
                    chrom_start_end.append(gene_info[0]['transcripts'][0]['annotations']['chromosome'])
                    chrom_start_end.append(transcript_data['start_position'])
                    chrom_start_end.append(transcript_data['end_position'])
                    transcript_coords.append(chrom_start_end)
            all_gene_coords.append(transcript_coords)
            transcript_coords = []
        return all_gene_coords
    
        
    def create_bed_file_iterable(self):
        # Specify the filename for the BED file
        # Writing to the BED file
        coords_for_bed = []
        for row in self.get_coord_mane_select_trans():
            chrom, start, end = row
            if self.padded_exons:
                start = int(start) - 50
                end = int(end) + 50
            line = str(chrom) + "\t" + str(start) + "\t" + str(end) + "\n"
            coords_for_bed.append(line)
        return coords_for_bed
