import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer as porter_stem

file_path = "test.csv"
dataset = pd.read_csv(file_path, encoding='unicode_escape')

sentences = dataset.iloc[:, 1].tolist()
sentiments = dataset.iloc[:, 2].tolist()

for sentence in sentences:
        tokens = word_tokenize(sentence)
        stemmed_tokens = [porter_stem().stem(token) for token in tokens]
        print(tokens)
        print(stemmed_tokens)

