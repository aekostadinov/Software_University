command_line = input().lower().split()
dict_words = {}

for word in command_line:
    if word not in dict_words:
        dict_words[word] = 0
    dict_words[word] += 1

for key,value in dict_words.items():
    if value % 2 != 0:
        print(key,end=" ")
