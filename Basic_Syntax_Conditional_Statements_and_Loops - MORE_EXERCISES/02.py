command = input()
lst = []

for i in range(len(command)):
    if command[i].isupper():
        lst.append(i)
print(lst)