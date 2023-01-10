def reversed_words():
    r_words = []
    words = set()
    for line in open("words.txt", encoding="utf-8"):
        words.add(line.strip())
    for word in words:
        if word[::-1] in words and (word, word[::-1]) not in r_words:
           r_words.append((word, word[::-1]))
    r_words.sort()
    return r_words
