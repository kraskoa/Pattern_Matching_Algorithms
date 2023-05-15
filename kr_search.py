# Dla ciebie Krzysiu zostal ten algorytm Karpa-Rabina i klasyczne sklejenie reszty maina
# Wstaw na poczatku definicji swojej funkcji cos na zasadzie:
#     lp = len(pattern)
#     lt = len(text)
#     if lp > lt:
#         return None
#     elif lp == lt:
#         if pattern == text:
#             return [0]
#         else:
#             return None
#     else:
#         {definicja funkcji}
# Bedzie sensowna spojnosc implementacji wtedy
def hash(text):
    hash_value = 0
    mod = 101
    base = 256
    for letter in text:
        hash_value = (hash_value * base + ord(letter)) % mod
    return hash_value


def kr_search(pattern, text):
    """
    Params:
    pattern (str) - searched text pattern
    text (str) - string to search for patterns in
    Returns:
    occurences (list) - list of pattern starting indexes in text
    """
    lp = len(pattern)
    lt = len(text)
    if lp > lt:
        return None
    elif lp == lt:
        if pattern == text:
            return [0]
        else:
            return None
    else:
        pass


def main():
    text = "abr"
    text2 = "hi"
    text3 = "bra"
    print(hash(text))
    print(hash(text2))
    print(hash(text3))


if __name__ == "__main__":
    main()
