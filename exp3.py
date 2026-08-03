import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')

text = "playing played plays player"

words = word_tokenize(text)

stemmer = PorterStemmer()

print("Original Words:", words)

print("\nStemmed Words:")
for word in words:
    print(word, "->", stemmer.stem(word))