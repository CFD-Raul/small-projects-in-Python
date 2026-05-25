# You are a text reviewer and need to identify very long words in a paragraph.
# You focus on making texts easier to read, so you want to detect words that have more than 10 letters and highlight them.

# You should create a program that receives a text input and displays all words that contain more than 10 letters.
# If no long words are found, you should inform the user.

# Example input:

# Enter a text: Structured programming improves the development of computational systems

# Expected output:

# Long words found: structured, programming, development, computational

# If no long words are found:

# No long words were found in the text.

# \

def long_words(text):
    words = text.split()
    return [w for w in words if len(w) > 10]

def long_words_check(text):
    result = long_words(text)
    if result:
        return f"{len(result)} long words were found: {result}"
    else:
        return "No long words were found."


text = input("Enter a text: ")
print(long_words_check(text))