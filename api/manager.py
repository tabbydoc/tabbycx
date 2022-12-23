from traceback import format_exc
from typing import List
from fastapi import UploadFile
from data_struct.table import Table, segmentate, discriminate, functional_analysis
from html_parse.html_parser import parse
from proposals.tomate.Tomate import TomateExtractor


class TabbyCxManager(object):

    def __init__(self, method="tomate", normalization="min-max-global",
                 clustering_features=['style', 'syntax', 'structural', 'semantic'],
                 text_metadata_dict=None) -> None:
        self.method = method
        self.normalization = normalization
        self.clustering_features = clustering_features
        self.text_metadata_dict = text_metadata_dict
        if self.method == "tomate":
            self.model = TomateExtractor()

    def parse_html(self, file: UploadFile) -> List[Table]:
        result = []
        tables = parse(file)
        for table in tables:
            try:
                segmentate(table, True, False, "", self.normalization, self.text_metadata_dict)
                if not discriminate(table):
                    continue
                functional_analysis(table, self.clustering_features, self.dimensionality_reduction,
                                    self.clustering_method)
                self.model.process(table)
            except:
                table.error = format_exc()

            result.append(table)

        return result