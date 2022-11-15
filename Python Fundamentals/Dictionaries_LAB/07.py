count = int(input())
dict_synonyms = {}

for _ in range(count):
    word = input()
    synonym = input()
    if word not in dict_synonyms:
        dict_synonyms[word] = []
    dict_synonyms[word].append(synonym)

for word, synonyms in dict_synonyms.items():
    print(f"{word} - {', '.join(dict_synonyms[word])}")