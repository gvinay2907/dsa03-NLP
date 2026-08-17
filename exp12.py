grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"], ["likes"]]
}

def earley_parse(words):
    n = len(words)
    chart = [[] for _ in range(n + 1)]

    chart[0].append(("S", ["NP", "VP"], 0, 0))

    for i in range(n + 1):
        changed = True

        while changed:
            changed = False

            for lhs, rhs, dot, start in chart[i]:

                # Prediction
                if dot < len(rhs) and rhs[dot] in grammar:
                    symbol = rhs[dot]

                    for rule in grammar[symbol]:
                        item = (symbol, rule, 0, i)

                        if item not in chart[i]:
                            chart[i].append(item)
                            changed = True

                # Completion
                elif dot == len(rhs):
                    for item in chart[start]:
                        lhs2, rhs2, dot2, start2 = item

                        if dot2 < len(rhs2) and rhs2[dot2] == lhs:
                            new_item = (
                                lhs2, rhs2, dot2 + 1, start2
                            )

                            if new_item not in chart[i]:
                                chart[i].append(new_item)
                                changed = True

        # Scanning
        if i < n:
            for lhs, rhs, dot, start in chart[i]:
                if dot < len(rhs) and rhs[dot] == words[i]:
                    chart[i + 1].append(
                        (lhs, rhs, dot + 1, start)
                    )

    return ("S", ["NP", "VP"], 2, 0) in chart[n]


sentence = input("Enter a sentence: ").lower().split()

if earley_parse(sentence):
    print("Sentence is accepted.")
else:
    print("Sentence is rejected.")