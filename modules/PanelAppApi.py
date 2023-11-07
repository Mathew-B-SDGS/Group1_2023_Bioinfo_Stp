import requests

api_url = "https://panelapp.genomicsengland.co.uk/api/v1/panels"


class ApiCallsSadie:

    def get_panels_for_genomic_test(self):
        endpoint = f"{api_url}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve panels")
            return None

    def return_specific_panel(self, test_code):
        for x in self.get_panels_for_genomic_test['results']:
            if test_code in x['relevant_disorders']:
                return x


# specific_panel = return_specific_panel('R169')
# print(specific_panel)
# panels = get_panels_for_genomic_test()
# #print(panels)
