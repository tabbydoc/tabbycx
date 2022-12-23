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

    def train(self, tables):
        pass

    def predict(self, table):
        with open(PATH_ORIGINAL_TABLE % table['_id'], 'rb') as fp:
            source = load(fp)
        source.element = soup(source.element)
        segmentate(source, add_image_text=True, add_link_urls=False, base_url=source.url,
                   normalization=self.normalization, text_metadata_dict=METADATA_CORPUS)
        discount_time = cpu_time() - discount_time
        try:
            functional_analysis(source, self.clustering_features, self.dimensionality_reduction, self.clustering_method)
            structural_analysis(source)
            predicted_table = [[FUNCTION_NAMES_PREDICTION[cell] for cell in row] for row in source.functions]
        except:
            print_exc()
        return predicted_table, discount_time


evaluate(TomateExtractor, 'tomate')