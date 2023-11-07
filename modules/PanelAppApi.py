import requests
# Specifying the API endpoint URL
api_url = "https://panelapp.genomicsengland.co.uk/api/v1/panels"

# Make a request to the API to retrieve the panels, with an filtering criteria
class ApiCallsSadie:

    def get_panels_for_genomic_test(self):
        endpoint = f"{api_url}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve panels")
            return None
# Specify the ID of the panel you want to retrieve, which looks into the relevant disorders to get the R number
    def return_specific_panel(self, test_code):
        panels = self.get_panels_for_genomic_test()
        for x in panels['results']:
            if test_code in x['relevant_disorders']:
                return x

#code = 'R169'
#obj = ApiCallsSadie()
#print(obj.return_specific_panel(code))

# specific_panel = return_specific_panel('R169')
# print(specific_panel)
# panels = get_panels_for_genomic_test()
# #print(panels)
