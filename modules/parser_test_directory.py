import pandas as pd


class Parser:
    """Parses the NGTD to the app"""
    def __init__(self,):
        self.df = pd.read_excel('./resources/Rare-and-inherited-disease-' +
                                'national-genomic-test-directory-version-' +
                                '5.1.xlsx', header=1)

    def parse(self, r_code):
        matching_rows = self.df[self.df.iloc[:, 0] == r_code.upper()]
        return matching_rows
