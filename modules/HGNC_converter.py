import requests

class HgncConverter ():
    """ convert HGNC symbols to Ensembl IDs and stuff"""

    def __init__(self, hgnc_input ):
        try:
            self.hgnc = int(hgnc_input.strip("HGNC:"))
        except ValueError:
            print("HGNC ID must be an integer")
        
        try: 
            self.ensembl_id = self.hgnc_id_api_query()["response"]["docs"][0]["ensembl_gene_id"]
        except KeyError:
            print("HGNC ID not found")
        finally:
            self.completed = True
    
    def __repr__(self):
        return f"HGNC ID: {self.hgnc} \nEnsembl ID: {self.ensembl_id} \nCompleted: {self.completed}" 

    def hgnc_id_api_query(self):
        """ querey the HGNC api for the ensembl ID"""
        url = "https://rest.genenames.org/fetch/hgnc_id/"
        target_url = url + self.hgnc
        response = requests.get(target_url, headers={"Accept": "application/json"})
        if response.status_code == 200:
            return response.json()
        else:
            return "error"
    
    def ensembl_id_api_query(self):
        """ querey the HGNC api for the ensembl ID"""
        url = "" # need to find the right url 
        target_url = url + self.hgnc
        response = requests.get(target_url, headers={"Accept": "application/json"})
        if response.status_code == 200:
            return response.json()
        else:
            return "error"

obj_test = HgncConverter("4982").hgnc_id_api_query()
print(obj_test["response"]["docs"][0]["ensembl_gene_id"])

