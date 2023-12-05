import pytest
import re
from modules.bedmake import RCodeToBedFile


class TestBedmake():
    """Tests each function within RCodeToBedFile class"""

    def setup_method(self):
        """Set up with test code and reference genome to be used throughpout
        tests
        """
        self.test_code = 'R207'
        self.ref_genome = 'GRCh38'
        self.bedmake = RCodeToBedFile(self.test_code, self.ref_genome)
        self.get_coords = self.bedmake.get_coords_for_bed()

    def test_get_panel_for_genomic_test(self):
        """Check that the correct panel is retrieevd from the PanelApp API
        by checking the panel ID for R207"""
        panel = self.bedmake.get_panel_for_genomic_test()
        assert panel['id'] == 143

    def test_extract_genes_hgnc(self):
        """Check that the fucntion returns a list of genes in HGNC format"""
        genes = self.bedmake.extract_genes_hgnc()
        regex = r"^HGNC:\d*"
        for gene in genes:
            assert re.match(regex, gene)

    def test_get_coords_for_bed(self):
        """Check the function returns a list of lists each with three 
        elements (chrom, start pos, end pos)
        """
        coordinates = self.get_coords
        for coord in coordinates[0]:
            assert len(coord) == 3

    def test_pad_bed_files(self):
        """Check that the output of pad_bed_files returns coordinates with
        50 bp padding by comparing to orginal coords
        """
        coordinates = self.get_coords
        padded_coordinates = self.bedmake.pad_bed_files()
        unpadded_coord = coordinates[0][1]
        padded_coord = padded_coordinates[1]
        assert unpadded_coord[1] == padded_coord[1] + 50
        assert unpadded_coord[2] == padded_coord[2] - 50

    def test_create_string_bed(self):
        """Check that a string type is output"""
        string_bed = self.bedmake.create_string_bed()
        assert type(string_bed) is str



    
