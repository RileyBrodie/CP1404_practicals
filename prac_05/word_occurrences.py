words = {}

text = str(input("Text: ")).split(" ")

for word in text:
    try:
        words[word] += 1
    except KeyError:
        words[word] = 1

max_length = 0
for word in words:
    word_length = len(word)
    if word_length > max_length:
        max_length = word_length

for word in words:
    print("{:{}} = {}".format(word, max_length, words[word]))
