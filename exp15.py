grammar = {
    "S": [
        (["NP", "VP"], 1.0)
    ],

    "NP": [
        (["Det", "N"], 0.6),
        (["N"], 0.4)
    ],

    "VP": [
        (["V", "NP"], 1.0)
    ],

    "Det": [
        (["the"], 0.5),
        (["a"], 0.5)
    ],

    "N": [
        (["cat"], 0.5),
        (["dog"], 0.5)
    ],

    "V": [
        (["sees"], 0.5),
        (["likes"], 0.5)
    ]
}


def parse(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and words[pos] == symbol:
            return pos + 1, 1.0
        return None

    best_result = None

    for rule, probability in grammar[symbol]:
        current_pos = pos
        total_probability = probability

        for item in rule:
            result = parse(item, words, current_pos)

            if result is None:
                break

            current_pos, child_probability = result
            total_probability *= child_probability
        else:
            if best_result is None or total_probability > best_result[1]:
                best_result = (current_pos, total_probability)

    return best_result


sentence = input("Enter a sentence: ").lower().split()

result = parse("S", sentence, 0)

if result and result[0] == len(sentence):
    print("Sentence is accepted.")
    print("Probability:", result[1])
else:
    print("Sentence cannot be parsed.")