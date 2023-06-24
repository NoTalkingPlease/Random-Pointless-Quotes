import random

# Lists of words from different categories
nouns = ["cat", "banana", "desk", "jupiter", "shoe"]
adjectives = ["purple", "enormous", "silly", "sparkling", "slimy"]
verbs = ["dance", "sing", "fly", "jump", "wiggle"]

def generate_random_quote():
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    verb = random.choice(verbs)

    quote = f"The {adjective} {noun} {verb}s in the moonlight."
    return quote

def generate_multiple_quotes(num_quotes):
    quotes = []
    for _ in range(num_quotes):
        quote = generate_random_quote()
        quotes.append(quote)
    return quotes

# Generate and print 5 random quotes
random_quotes = generate_multiple_quotes(5)
for quote in random_quotes:
    print(quote)
