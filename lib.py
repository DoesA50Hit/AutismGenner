from words import adjectives, nouns  # Import adjectives and nouns from words.py

# ===========================
# Word List Setup
# ===========================

# Convert tuples to lists and combine them into a single WORDS list
WORDS = [word for word in list(adjectives) + list(nouns) if isinstance(word, str) and word.isalpha() and len(word) > 2]

# ===========================
