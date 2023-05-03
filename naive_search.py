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
