"""Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique
ones. On the first line, you will receive an integer N. On the next N lines, you will receive a username.
Print the collection on the console (the order does not matter):"""

count_of_names = int(input())
set_of_names = {input() for _ in range(count_of_names)}
for name in set_of_names:
    print(name)


### Variant 2 ###

# print(*{input() for _ in range(int(input()))}, sep="\n")