
# You are an English language teacher and want a program that counts how many vowels appear in a text typed by your students.
# This will help you analyze the structure of the words they use.

# Create a program that asks for a text input and displays how many vowels (a, e, i, o, u, y) it contains.

# Example input:

# Enter a text: Python programming is very useful.

# Expected output:

# The text contains 11 vowels.

# \

import re

def count_vowels(text):

    vowels = re.findall(r"[aeiouy]", text, re.IGNORECASE)
    return len(vowels)


text = input("Enter a text: ").strip()

print(f"The text contains {count_vowels(text)} vowels.")