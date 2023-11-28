import pytest
from modules.bedmake import RCodeToBedFile


class TestRCodetoBedFile:

    def setUp(self):
        self.test_r_code = 'R201'
        self.ref_genome = 'GRCh38'
        self.include_exon = 'Transcript'
        self.clas = RCodeToBedFile(test_code=self.test_r_code, ref_genome=self.ref_genome,
                                       include_exon=self.include_exon, padded=False)
    
    def test_get_panel_for_genomic_test(self):
        panel_app_response = 
        panel_info = panel_app_response.get_panel_for_genomic_test()
        panel_name = panel_info['name']
        assert panel_name == 'Atypical haemolytic uraemic syndrome'

        
