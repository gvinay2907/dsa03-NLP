grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"], ["likes"]]
}


def parse(symbol, words, pos):
    # Terminal symbol
    if symbol not in grammar:
        if pos < len(words) and words[pos] == symbol:
            return pos + 1, symbol
        return None

    # Non-terminal symbol
    for rule in grammar[symbol]:
        current_pos = pos
        children = []
        success = True

        for item in rule:
            result = parse(item, words, current_pos)

            if result is None:
                success = False
                break

            current_pos, child = result
            children.append(child)

        if success:
            return current_pos, (symbol, children)

    return None


def print_tree(tree, level=0):
    if isinstance(tree, str):
        print("  " * level + tree)
    else:
        symbol, children = tree

        print("  " * level + symbol)

        for child in children:
            print_tree(child, level + 1)


# Input
sentence = input("Enter a sentence: ").lower().split()

# Parsing
result = parse("S", sentence, 0)

# Output
if result is not None and result[0] == len(sentence):
    print("\nSentence is accepted.")
    print("\nParse Tree:")
    print_tree(result[1])
else:
    print("\nSentence is rejected.")