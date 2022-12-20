def longest_word():
    data = []
    largestWord = 0
    for line in open("words.txt", encoding="utf-8"):
        data.append(line.strip())
    for word in data:
        if 28 < len(word):
            largestWord = word
    return largestWord
print(longest_word())
