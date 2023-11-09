import requests


class HgncConverter ():
    """class that takes the HGNC symbols from the panel app to Ensembl IDs and get the list of transcripts for each gene"""

    def __init__(self, hgnc_input):
        try:
            self.hgnc = str(int(hgnc_input.strip("HGNC:")))
            
        except ValueError:
            print("HGNC ID must be an integer")

        try:
            self.ensembl_id = self.hgnc_id_api_query(
            )["response"]["docs"][0]["ensembl_gene_id"]
        except Exception as e:
            print(e)
        finally:
            self.completed = True

    def __repr__(self):
        return f"HGNC ID: {self.hgnc} \nEnsembl ID: {self.ensembl_id} \nCompleted: {self.completed}"

    def hgnc_id_api_query(self):
        """ querey the HGNC api for the ensembl ID"""
        url = "https://rest.genenames.org/fetch/hgnc_id/"
        target_url = url + self.hgnc
        response = requests.get(target_url, headers={
                                "Accept": "application/json"})
        if response.status_code == 200:
            return response.json()
        else:
            return "error"

    def ensembl_id_api_query(self, full_transcript_list=False):
        """ querey the HGNC api for the ensembl ID
        if full_transcript_list is set to True, the function will return a list of all the transcripts for the gene
        """
        url = "https://rest.ensembl.org/lookup/id/"

        #check to see if Whole expansion is wanted. If so, add the expand=1 to the url
        if full_transcript_list:
            target_url = url + self.ensembl_id +"?expand=1"
        else:
            target_url = url + self.ensembl_id + "?"
        
        response = requests.get(target_url, headers={ "Content-Type" : "application/json"})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API request failed for {repr(self)} with status code {response.status_code}")

if __name__ == "__main__":

    obj_test = HgncConverter("4982")  # Create an instance
    result = obj_test.ensembl_id_api_query(full_transcript_list=True)  # Call the method on the instanc

    # print(result)
    for i in result["Transcript"]:
        print(i["Parent"])
