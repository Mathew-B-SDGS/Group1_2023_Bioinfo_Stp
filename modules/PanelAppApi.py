import requests

api_url = "https://panelapp.genomicsengland.co.uk/api/v1/panels"


class ApiCallsSadie():
    def __init__(self, test_code):
        self.test_code = test_code

    # Make a request to the API to retrieve all panels
    def get_panels_for_genomic_test(self):
        endpoint = f"{api_url}"
        print(endpoint)
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve panels")
            return None

    def return_specific_panel(self):
        # Specify the test R code associated with the panel
        # you want to retrieve and return panel information
        R_test_code = self.test_code
        panel_list = self.get_panels_for_genomic_test()
        for panel in panel_list['results']:
            if R_test_code.upper() in panel['relevant_disorders']:
                return panel

    def return_disease_name(self):
        # extract panel name for next gene api query
        specific_panel = self.return_specific_panel()
        disease_name = specific_panel['name']
        return disease_name

    def query_api_for_genes(self):
        # query api for gene name using panel primary key
        # which is disease name from previous function
        disease_name = self.return_disease_name()
        url = f"{api_url}"
        endpoint = url + "/" + f"{disease_name}" + "/genes/"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve panels")
            return None

    def extract_genes_hgnc(self):
        # extract gene name from json from above api query
        gene_list = []
        gene_information = self.query_api_for_genes()
        for gene in gene_information['results']:
            gene_list.append(gene['gene_data']['hgnc_id'])
