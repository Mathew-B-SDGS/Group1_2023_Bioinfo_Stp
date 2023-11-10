import requests

api_url = "https://panelapp.genomicsengland.co.uk/api/v1/panels/"


class ApiCallsbyR():
    """
    Run code by calling class with R test code and desired reference genome
    """
    def __init__(self, test_code, ref_genome):
        self.test_code = test_code
        self.ref_genome = ref_genome

    # Make a request to the API to retrieve all panels
    def get_panel_for_genomic_test(self):
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

    def filter_coordinates(self):
        gene_locations = []
        gene_information = self.get_panel_for_genomic_test()
        for gene in gene_information['genes']:
            if self.ref_genome == 'GRCh37':
                gene_locations.append(
                    gene['gene_data']['ensembl_genes']['GRch37']['82']['location'])
            elif self.ref_genome == 'GRCh38':
                gene_locations.append(
                    gene['gene_data']['ensembl_genes']['GRch38']['90']['location'])
            else:
                print('Incorrect reference genome selected')
        return gene_locations

    def create_bed_structure(self):
        chrom_start_end = []
        list_of_coords_for_bed = []
        list_of_coords = self.filter_coordinates()
        for coordinate in list_of_coords:
            chrom_start_end.append(coordinate.split(':')[0])
            start = coordinate.split(':')[1]
            chrom_start_end.append(start.split('-')[0])
            chrom_start_end.append(coordinate.split('-')[1])
            list_of_coords_for_bed.append(chrom_start_end)
            chrom_start_end = []
        return list_of_coords_for_bed
    
    def create_bed_file(self):
        # Specify the filename for the BED file
        test_code = self.test_code 
        filename = test_code + '.bed'
        # Writing to the BED file
        with open(filename, mode='w') as file:
            for row in self.create_bed_structure():
                chrom, start, end = row
                file.write(f"{chrom}\t{start}\t{end}\n")

        print(f'BED file "{filename}" has been created successfully.')
