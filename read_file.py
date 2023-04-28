# Function that returns a given amount of random words from input file
import random


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