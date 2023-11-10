import requests 

base_url = "https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts_v2/HGNC%3A4982/mane_select/refseq/GRCh37?content-type=application%2Fjson"

class VariantValidatorRefseq:
    def get_refseq_transcripts(self):
# HTTP GET request to the API, using gene_id as a parameter
        endpoint = f"{base_url}"
        response = requests.get(endpoint)
 # If request successful, json will return data on ref seq transcripts
        if response.status_code == 200:
           return response.json()
        else:
         print("Failed to retrieve refseq transcripts")
         return None

def return_mane_select_transcripts(self, HGVS):
    refseq_transcripts = self.get_refseq_transcripts()
    




