"""Write a program to flatten several lists of numbers received in the following format:
    -String with numbers or empty strings separated by "|"
    -Values are separated by spaces (" ", one or several)
    -Order the output list from the last to the first matrix sub-lists and their values
from left to right as shown below"""
### Variant 1 ###
# console_string = input().split("|")
# matrix = []
# for string in console_string:
#     num = string.split()
#     matrix.append(num)
# result = []
# for row in range(len(matrix) - 1, -1, -1):
#     result += matrix[row]
# print(' '.join(result))

### Variant 2 ###
matrix = input().split("|")[::-1]
for row in range(len(matrix)):
    for element in matrix[row].split():
        print(element,end=' ')
