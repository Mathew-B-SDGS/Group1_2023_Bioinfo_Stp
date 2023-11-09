import requests

class HgncConverter ():
    """ convert HGNC symbols to Ensembl IDs and stuff"""

    def __init__(self, hgnc_input ):
        self.hgnc = hgnc_input

    def api_querey(self):
        """ querey the HGNC api for the ensembl ID"""
        url = "https://rest.genenames.org/fetch/hgnc_id/"
        target_url = url + self.hgnc
        response = requests.get(target_url, headers={"Accept": "application/json"})
        if response.status_code == 200:
            return response.json()
        else:
            return "error"

obj_test = HgncConverter("4982")
print(obj_test.api_querey())