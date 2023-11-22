import requests

def get_refseq_transcripts(genome_build, variant_description, select_transcripts="all"):
    base_url = "https://rest.variantvalidator.org/VariantValidator/variantvalidator/GRCh37/"

    # Specify parameters in the URL path
    url = f"{base_url}?genome_build={genome_build}&variant_description={variant_description}&select_transcripts={select_transcripts}"

    # Set the headers to indicate that you want JSON response
    headers = {"content-type": "application/json"}

    # Make the request to Variant Validator API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Extract and print RefSeq transcripts
        transcripts = data.get('transcripts', [])
        if transcripts:
            print("RefSeq Transcripts:")
            for transcript in transcripts:
                transcript_id = transcript.get('transcript_id', 'N/A')
                gene_symbol = transcript.get('gene_symbol', 'N/A')
                print(f"Transcript ID: {transcript_id}, Gene: {gene_symbol}")
        else:
            print("No RefSeq transcripts found for the gene/transcript.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Example parameters (replace with your own)
    genome_build = "GRCh37"
    variant_description = "NM_007294.4"
    select_transcripts = "refseq_select"  # Change this based on your preference

    get_refseq_transcripts(genome_build, variant_description, select_transcripts)
