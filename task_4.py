def reversed_words():
    r_words = []
    words = set()
    for line in open("words.txt", encoding="utf-8"):
        words.add(line.strip())
    for word in words:
       if word[::-1] in words:
           r_words.append((word and word[::-1]))
    r_words.sort()
    return r_words
