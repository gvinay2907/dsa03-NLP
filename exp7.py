import nltk
nltk.download('averaged_perceptron_tagger_eng')
text = input("Enter a sentence: ")

words = text.split()

print(nltk.pos_tag(words))