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

    def ensembl_id_api_query(self):
        """ query the HGNC api for the ensembl ID
        ***removed*** - if full_transcript_list is set to True, the function will return a list of all the transcripts for the gene
        """
        url = "https://rest.ensembl.org/lookup/id/"

        target_url = url + self.ensembl_id + "?expand=1"

        print(target_url)
        response = requests.get(target_url, headers={
                                "Content-Type": "application/json"})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"API request failed for {repr(self)} with status code {response.status_code}")

    def ens_transcript_list(self):
        transcript_list = []
        ensembl_data = self.ensembl_id_api_query()
        for transcript in ensembl_data['Transcript']:
            transcript_list.append(transcript['id'])
        return transcript_list

# the below class depends on the result of transcript selection from the list output from ens_transcript_list
# it also uses the output of function ensembl_api_query
# not sure if this is better to be one class or two as they interact.


class CreateBed():
    """
    Takes selected  ENS transcript and creates bedfile
    The input is the transcript id which the user will need to select from ens_transcript_list output
    The user will also need to select if they want padded exons or whole transcript

    """

    def __init__(self, transcript_id, padded_exons=True):
        self.transcript_id = transcript_id
        self.ensembl_data = obj_test.ensembl_id_api_query() #information from the last class which I don't think is a good way to structure this
        self.padded_exons = padded_exons

    def get_transcript_coord(self):
        list_of_coords_for_bed = []
        chrom_start_end = []
        for transcript in self.ensembl_data['Transcript']:
            if transcript['id'] == self.transcript_id:
                if self.padded_exons:
                    for exon in transcript['Exon']:
                        chrom_start_end.append(exon['seq_region_name'])
                        chrom_start_end.append(exon['start'])
                        chrom_start_end.append(exon['end'])
                        list_of_coords_for_bed.append(chrom_start_end)
                        chrom_start_end = []
                else:
                    chrom_start_end.append(transcript['seq_region_name'])
                    chrom_start_end.append(transcript['start'])
                    chrom_start_end.append(transcript['end'])
                    list_of_coords_for_bed.append(chrom_start_end)

                return list_of_coords_for_bed

    def create_bed_file_iterable(self):
        # Specify the filename for the BED file
        # Writing to the BED file
        list_of_coords_for_bed = []
        for row in self.get_transcript_coord():
            chrom, start, end = row
            if self.padded_exons:
                start = int(start) - 50
                end = int(end) + 50
            line = str(chrom) + "\t" + str(start) + "\t" + str(end) + "\n"
            list_of_coords_for_bed.append(line)
        return list_of_coords_for_bed


if __name__ == "__main__":

    obj_test = HgncConverter("4982")  # Create an instance
    second_obj = CreateBed('ENST00000536185', False)
    result = obj_test.ens_transcript_list()  # Call the method on the instanc
    result_2 = second_obj.create_bed_file_iterable()
