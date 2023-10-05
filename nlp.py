import nltk
import spacy
from nltk.stem import PorterStemmer
from nltk.tokenize import NLTKWordTokenizer
from nltk.corpus import stopwords

stemmer = PorterStemmer()
tokenizer = NLTKWordTokenizer()

text = "Virat Kohli was a captain of Indian Cricket Team. He is batting on number 2 today. "
tokenized_words = tokenizer.tokenize(text)
print(tokenized_words)
tokenized_words = [word for word in tokenized_words if word not in stopwords.words("english")]
print(tokenized_words)

# print(stemmer.stem(text))
print(stemmer.stem("writing"))
# print(stopwords.words("english"))


# nlp = spacy.load("en_core_web_sm")
# nlp