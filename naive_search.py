def naive_search(pattern, text):
    """
    Params:
    pattern (str) - searched text pattern
    text (str) - string to search for patterns in
    Returns:
    occurences (list) - list of pattern starting indexes in text
    """
    occurences = []
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
        for i in range(lt - lp + 1):
            j = 0
            while j < lp:
                if text[i + j] != pattern[j]:
                    break
                j += 1
            if j == lp:
                occurences.append(i)
        return occurences


def main():
    pattern = ""
    text = ""
    print(naive_search(pattern, text))
    pattern_equal_text = "abc"
    text_equal_pattern = "abc"
    print(naive_search(pattern_equal_text, text_equal_pattern))
    pattern_not_in_text = "abc"
    text_not_in_pattern = "def"
    print(naive_search(pattern_not_in_text, text_not_in_pattern))
    pattern_longer_than_text = "abcdef"
    text_shorter_than_pattern = "abc"
    print(naive_search(pattern_longer_than_text, text_shorter_than_pattern))


if __name__ == "__main__":
    main()
