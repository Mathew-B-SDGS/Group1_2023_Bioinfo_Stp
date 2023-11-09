import requests

api_url = "https://panelapp.genomicsengland.co.uk/api/v1/panels"


class ApiCallsSadie:
    def __init__(self, test_code):
        self.test_code = test_code
    # Make a request to the API to retrieve all panels
    def get_panels_for_genomic_test(self):
        endpoint = f"{api_url}/signedoff/"
        response = requests.get(endpoint)
        if response.status_code == 200:
           return response.json()
        else:
           print("Failed to retrieve panels")
           return None

    def return_specific_panel(self, R_test_code):
        # Specify the test R code associated with the panel
        # you want to retrieve and return panel information
        panel_list = self.get_panels_for_genomic_test()
        for panels in panel_list['results']:
            if R_test_code.upper() in panels['relevant_disorders']:
                return panels
   
 
        

