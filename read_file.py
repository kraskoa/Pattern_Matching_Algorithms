import random


# Function that returns a given length list of random words from file
def read_words_from_file(path, n):
    words_list = []
    final_list = []
    with open(path, "r") as file_handle:
        for line in file_handle:
            for word in line.split():
                words_list.append(word)
        final_list = random.choices(words_list, k=n)
        file_handle.close()
    return final_list


# Function that reads all the words from a file into a string
def read_whole_file(path):
    final_string = ""
    with open(path, "r") as file_handle:
        for line in file_handle:
            for word in line.split():
                final_string += f"{word} "
        file_handle.close()
    return final_string


# Function that returns a given length list of n first words from a file
def read_first_words(path, n):
    first_words = []
    with open(path, "r") as file_handle:
        for line in file_handle:
            for word in line.split():
                first_words.append(word)
                if len(first_words) == n:
                    return first_words
        file_handle.close()
    return first_words
