def generate_plural(word):
    # Words ending with s, x, z, ch, sh -> add "es"
    if word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"

    # Words ending with consonant + y -> replace y with ies
    elif word.endswith("y") and word[-2].lower() not in "aeiou":
        return word[:-1] + "ies"

    # Default rule -> add s
    else:
        return word + "s"


# Test words
words = ["cat", "bus", "box", "baby", "brush", "toy"]

print("Plural Forms:")
for word in words:
    print(word, "->", generate_plural(word))