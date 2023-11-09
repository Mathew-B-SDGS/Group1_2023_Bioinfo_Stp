import requests 

base_url = "https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts_v2/HGNC%3A4982/mane_select/refseq/GRCh37?content-type=application%2Fjson"


#def get_transcripts_from_gene_id(gene_id):
   # try:
        # HTTP GET request to the API, using gene_id as a parameter

response = requests.get(base_url)
        # If request successful, json will return data on ref seq transcripts
refseq_transcripts = response.json()
print (refseq_transcripts)


