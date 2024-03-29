def hash(text):
    hash_value = 0
    mod = 101
    base = 256
    for letter in text:
        hash_value = (hash_value * base + ord(letter)) % mod
    return hash_value


def next_hash(text, old_hash, old_letter, new_letter):
    mod = 101
    base = 256
    hash_value = (old_hash - ord(old_letter) * pow(base, len(text) - 1)) * base + ord(
        new_letter
    )
    return hash_value % mod


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
        occurences = []
        pattern_hash = hash(pattern)
        text_hash = hash(text[:lp])
        for i in range(lt - lp + 1):
            if pattern_hash == text_hash:
                if pattern == text[i : i + lp]:
                    occurences.append(i)
            if i < lt - lp:
                text_hash = next_hash(
                    text[i : i + lp], text_hash, text[i], text[i + lp]
                )
        return occurences


def main():
    # text = "Ibrahimovic"
    # text2 = "brahimovicJ"
    # print(hash(text))
    # print(hash(text2))
    # print(next_hash(text, hash(text), "I", "J"))

    pattern = ""
    text = ""
    print(kr_search(pattern, text))
    pattern_equal_text = "abc"
    text_equal_pattern = "abc"
    print(kr_search(pattern_equal_text, text_equal_pattern))
    pattern_not_in_text = "abc"
    text_not_in_pattern = "def"
    print(kr_search(pattern_not_in_text, text_not_in_pattern))
    pattern_longer_than_text = "abcdef"
    text_shorter_than_pattern = "abc"
    print(kr_search(pattern_longer_than_text, text_shorter_than_pattern))


if __name__ == "__main__":
    main()
