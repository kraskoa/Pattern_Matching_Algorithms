import time
import gc
from naive_search import naive_search
from kmp_search import kmp_search
from kr_search import kr_search
from test_pattern import random_text, random_pattern
from read_file import read_words_from_file, read_whole_file, read_first_words
from graph_maker import combined_3_graph_maker


def main():
    # Zgodnie z poleceniem sprawdzamy poprawnosc implementacji za pomoca random_text i random_pattern
    # Tworzymy testowy text i testowy pattern i odpalamy dla tego samego wszystkie 3 algorytmy
    # Wyprintujemy w konsoli cos na zasadzie "Algorithm testing: \nNaive search result: [1, 4, 6]\n KMP search result: [1, 4, 6] itd
    # KK: Ok, ogarniemy
    # Przed oddaniem trzeba usunac te komentarze XD
    # KK: E, a po co? XD
    text = random_text()
    pattern = random_pattern()
    print("ALGORITHM TESTING")
    print(f"Naive search result: {naive_search(pattern, text)}")
    print(f"KMP search result: {kmp_search(pattern, text)}")
    print(f"KR search result: {kr_search(pattern, text)}")

    # Nastepnie sprawdzamy jak algorytmy zachowuja sie dla plikow tekstowych
    print("FILE TESTING")
    naive_times = {}
    kmp_times = {}
    kr_times = {}
    number_of_first_words_list = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    pan_tadeusz = read_whole_file("pan_tadeusz.txt")

    for key in number_of_first_words_list:
        first_words = read_first_words("pan_tadeusz.txt", key)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for word in first_words:
            naive_search(word, pan_tadeusz)
        end = time.process_time()
        search_time = end - start
        if gc_old:
            gc.enable()
        naive_times[key] = search_time
    print("Naive search times:")
    print(naive_times)

    for key in number_of_first_words_list:
        first_words = read_first_words("pan_tadeusz.txt", key)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for word in first_words:
            kmp_search(word, pan_tadeusz)
        end = time.process_time()
        search_time = end - start
        if gc_old:
            gc.enable()
        kmp_times[key] = search_time
    print("KMP search times:")
    print(kmp_times)

    for key in number_of_first_words_list:
        first_words = read_first_words("pan_tadeusz.txt", key)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for word in first_words:
            kr_search(word, pan_tadeusz)
        end = time.process_time()
        search_time = end - start
        if gc_old:
            gc.enable()
        kr_times[key] = search_time
    print("KR search times:")
    print(kr_times)

    combined_3_graph_maker(
        naive_times,
        "Naive search",
        kmp_times,
        "KMP search",
        kr_times,
        "KR search",
        "Pan Tadeusz searching times",
    )


if __name__ == "__main__":
    main()
