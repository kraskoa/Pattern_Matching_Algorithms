def create_lps(pattern):
    lps = [0] * len(pattern)
    max_len = 0
    i = 1
    while i < len(pattern):
        if pattern[max_len] == pattern[i]:
            max_len += 1
            lps[i] = max_len
            i += 1
        else:
            if max_len != 0:
                max_len = lps[max_len - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(pattern, text):
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
        lps = create_lps(pattern)
        i = 0
        j = 0
        while (lt - i) >= (lp - j):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == lp:
                occurences.append(int(i - j))
                j = lps[j - 1]
            elif i < lt and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return occurences


def main():
    pattern = ""
    text = ""
    print(kmp_search(pattern, text))
    pattern_equal_text = "abc"
    text_equal_pattern = "abc"
    print(kmp_search(pattern_equal_text, text_equal_pattern))
    pattern_not_in_text = "abc"
    text_not_in_pattern = "def"
    print(kmp_search(pattern_not_in_text, text_not_in_pattern))
    pattern_longer_than_text = "abcdef"
    text_shorter_than_pattern = "abc"
    print(kmp_search(pattern_longer_than_text, text_shorter_than_pattern))


if __name__ == "__main__":
    main()
