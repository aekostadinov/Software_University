"""Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
The input will be provided as a single string."""

text = input()
for index in range(0,len(text)):
    if text[index] == ":":
        print(text[index:index + 2])


