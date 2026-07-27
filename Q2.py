import re

products = [
    "Laptop",
    "Laptop Bag",
    "Laptop Stand",
    "Mouse",
    "Keyboard",
    "Phone",
    "Phone Case",
    "Smart Phone",
    "Wireless Mouse"
]

# Search keyword
keyword = input("Enter Search Keyword: ")

# Exact Search
exact = [p for p in products if re.fullmatch(keyword, p, re.IGNORECASE)]

# Prefix Search
prefix = [p for p in products if re.match(keyword, p, re.IGNORECASE)]

# Suffix Search
suffix = [p for p in products if re.search(keyword + "$", p, re.IGNORECASE)]

# Partial Search
partial = [p for p in products if re.search(keyword, p, re.IGNORECASE)]

print("\nExact Match:", exact)
print("Prefix Match:", prefix)
print("Suffix Match:", suffix)
print("Partial Match:", partial)

print("\n----- Report -----")
print("Exact Matches:", len(exact))
print("Prefix Matches:", len(prefix))
print("Suffix Matches:", len(suffix))
print("Partial Matches:", len(partial))