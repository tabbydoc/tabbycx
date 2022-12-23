from traceback import print_exc

from data_struct.table import functional_analysis, structural_analysis


class TomateExtractor:

    def __init__(
            self,
            normalization='min-max-global',  # min-max-global, min-max-local, standard, softmax
            clustering_features=['style', 'syntax', 'structural'],  # any subset of those
            dimensionality_reduction='feature-agglomeration',  # off, pca, feature-agglomeration
            clustering_method='agglomerative'  # k-means, agglomerative
    ):
        self.normalization = normalization
        self.clustering_features = clustering_features
        self.dimensionality_reduction = dimensionality_reduction
        self.clustering_method = clustering_method
        self.FUNCTION_NAMES_PREDICTION = {
            -1: 'data',
            0: 'data',
            1: 'meta-data',
            2: 'data',
            3: 'data',
            4: 'data',
            5: 'meta-data',
            6: 'data'
        }

    def train(self, tables):
        pass

    def process(self, table):
        try:
            functional_analysis(table, self.clustering_features, self.dimensionality_reduction, self.clustering_method)
            structural_analysis(table)
            predicted_table = [[self.FUNCTION_NAMES_PREDICTION[cell] for cell in row] for row in table.functions]
        except:
            table.error = print_exc()

        return predicted_table


