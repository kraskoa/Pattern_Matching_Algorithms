import random


# Function that returns a random test text created with letters 'A' and 'B'
# It's length is always between 20 and a 1000
def random_text():
    text = ""
    letters = ["A", "B"]
    text_length = random.randint(20, 1000)
    for i in range(text_length):
        text += random.choice(letters)
    return text


# Function that returns a random test pattern created with letters 'A' and 'B'
# It's length is always between 2 and 8
def random_pattern():
    pattern = ""
    letters = ["A", "B"]
    pattern_length = random.randint(2, 8)
    for i in range(pattern_length):
        pattern += random.choice(letters)
    return pattern
