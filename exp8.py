import random

text = input("Enter words: ")

words = text.split()

tags = ["NN", "VB", "JJ", "RB"]

print("Assigned Tags:")
for word in words:
    print(word, "->", random.choice(tags))