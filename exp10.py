text = input("Enter words: ")

words = text.split()

for word in words:
    tag = "NN"

    if word.endswith("ing"):
        tag = "VBG"
    elif word.endswith("s"):
        tag = "NNS"

    print(word, "->", tag)