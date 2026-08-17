grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"], ["likes"]]
}

def parse(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and words[pos] == symbol:
            return pos + 1, symbol
        return None

    for rule in grammar[symbol]:
        current_pos = pos
        children = []

        for item in rule:
            result = parse(item, words, current_pos)

            if result is None:
                break

            current_pos, child = result
            children.append(child)
        else:
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


sentence = input("Enter a sentence: ").lower().split()

result = parse("S", sentence, 0)

if result and result[0] == len(sentence):
    print("\nParse Tree:")
    print_tree(result[1])
else:
    print("Sentence cannot be parsed.")