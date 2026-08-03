import nltk
from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# List of words
words = ["playing", "played", "plays", "player",
         "running", "studies", "studying", "happiness"]

print("Word\t\tStem")

for word in words:
    print(f"{word}\t\t{ps.stem(word)}")