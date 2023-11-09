import requests

api_url = "https://panelapp.genomicsengland.co.uk/api/v1/panels/"


class ApiCallsbyR():
    def __init__(self, test_code):
        self.test_code = test_code
      
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
