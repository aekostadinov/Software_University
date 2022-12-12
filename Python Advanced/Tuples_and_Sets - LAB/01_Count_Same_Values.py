"""You will be given numbers separated by a space. Write a program that prints the number of occurrences of each
 number in the format "{number} - {count} times". The number must be formatted to the first decimal point."""


tupple = tuple(float(x) for x in input().split())
occurrences = {}
for element in tupple:
    if element not in occurrences:
        occurrences[element] = 0
    occurrences[element] += 1
for num, count in occurrences.items():
    print(f"{num} - {count} times",end='\n')