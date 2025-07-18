# 1. Convert the ages to a set and compare the length of the list and the set
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)

print("Length of list:", len(ages))       # 8
print("Length of set:", len(ages_set))    # 5
print("List is bigger" if len(ages) > len(ages_set) else "Set is bigger or equal")

# 2. Explain the difference between: string, list, tuple, and set
# String: Immutable sequence of characters, e.g., "Hello"
# List: Ordered, mutable collection, e.g., [1, 2, 3]
# Tuple: Ordered, immutable collection, e.g., (1, 2, 3)
# Set: Unordered, mutable, no duplicates, e.g., {1, 2, 3}

# 3. Unique words in the sentence
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
