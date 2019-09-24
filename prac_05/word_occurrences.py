words = {}

text = str(input("Text: ")).split(" ")

for word in text:
    try:
        words[word] += 1
    except KeyError:
        words[word] = 1

print(words)
