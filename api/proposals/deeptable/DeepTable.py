class DeepTableExtractor:
    def __init__(self):
        self.MAX_COL = 9
        self.MAX_COL_LENGTH = 9
        self.MAX_CELL_LENGTH = 4
        self.tokenizer = Tokenizer()
        self.model = load_model('./deep_table_model.hdf5')

    def train(self, tables):
        texts = ["XXX"] + [' '.join(text_to_word_sequence(' '.join(sum(x['texts'], [])), lower=True)) for x in tables]
        self.tokenizer.fit_on_texts(texts)

    def transform_tables(self, tables):

        data = np.zeros((int(len(tables) * 0.75), self.MAX_COL, self.MAX_COL_LENGTH, self.MAX_CELL_LENGTH),
                        dtype='int32')
        X = tables[0:int(len(tables) * 0.75)]
        print(X[0])
        # y = y[0:int(len(y) * 0.75)]

        for i, table in enumerate(X):
            for j, col in enumerate(table['texts']):
                if j < self.MAX_COL:
                    for k, cell in enumerate(col):
                        if k < self.MAX_COL_LENGTH:
                            z = 0
                            for _, word in enumerate(text_to_word_sequence(cell, lower=True)):
                                if z < self.MAX_CELL_LENGTH:
                                    if self.tokenizer.word_index.get(word) is not None:
                                        data[i, j, k, z] = self.tokenizer.word_index[word]
                                        z = z + 1

        return data, np.array(y), self.tokenizer.word_index

    def predict(self, table):
        data = np.zeros((1, self.MAX_COL, self.MAX_COL_LENGTH, self.MAX_CELL_LENGTH), dtype='int32')
        rows, cols = len(table['texts']), len(table['texts'][0])
        for j, col in enumerate(array(table['texts'])):
            if j < self.MAX_COL:
                for k, cell in enumerate(col):
                    if k < self.MAX_COL_LENGTH:
                        z = 0
                        for _, word in enumerate(text_to_word_sequence(cell, lower=True)):
                            if z < self.MAX_CELL_LENGTH:
                                if self.tokenizer.word_index.get(word) is not None:
                                    data[0, j, k, z] = self.tokenizer.word_index[word]
                                    z = z + 1

        try:
            prediction = self.model.predict(data, verbose=0)
        except:
            print('except')

        pred = [p.tolist().index(max(p.tolist())) for p in prediction]
        cls = pred[0]
        res = [['data' for _ in range(cols)] for _ in range(rows)]
        if cls == 0 or cls == 2:
            res[0] = ['meta-data' for _ in range(cols)]
        if cls == 1 or cls == 2:
            for r in range(rows):
                res[r][0] = 'meta-data'
        return res, 0