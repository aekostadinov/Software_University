num = input()
lst = []

for ch in num:
    lst.append(ch)
lst = sorted(lst, reverse=True)
print(''.join(lst))
