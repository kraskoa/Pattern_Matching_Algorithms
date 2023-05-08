from naive_search import naive_search
from kmp_search import kmp_search
from test_pattern import random_text, random_pattern
from read_file import read_words_from_file, read_whole_file, read_first_words


def main():
    # Zgodnie z poleceniem sprawdzamy poprawnosc implementacji za pomoca random_text i random_pattern
    # Tworzymy testowy text i testowy pattern i odpalamy dla tego samego wszystkie 3 algorytmy
    # Wyprintujemy w konsoli cos na zasadzie "Algorithm testing: \nNaive search result: [1, 4, 6]\n KMP search result: [1, 4, 6] itd
    # Przed oddaniem trzeba usunac te komentarze XD
    text = random_text()
    pattern = random_pattern()
    print("ALGORITHM TESTING")
    print(f"Naive search result: {naive_search(pattern, text)}")


if __name__ == "__main__":
    main()
