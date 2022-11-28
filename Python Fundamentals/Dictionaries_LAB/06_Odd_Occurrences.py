"""Write a program that prints all elements from a given sequence of
words that occur an odd number of times (case-insensitive) in it.

· Words are given on a single line, space-separated.

· Print the result elements in lowercase, in their order of appearance."""




command_line = input().lower().split()
dict_words = {}

for word in command_line:
    if word not in dict_words:
        dict_words[word] = 0
    dict_words[word] += 1

for key,value in dict_words.items():
    if value % 2 != 0:
        print(key,end=" ")
