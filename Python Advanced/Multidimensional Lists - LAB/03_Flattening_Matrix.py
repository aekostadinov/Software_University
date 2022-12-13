"""Write a program that receives a matrix and print the flattened version of it.
On the first line, you will receive the number of a matrix's rows.On the next rows, you will get the
elements for each column separated with a comma and space."""
### Variant 1 ###
# rows = int(input())
# matrix = []
# for row in range(rows):
#     current_lst = [int(n) for n in input().split(", ")]
#     matrix += current_lst
# print(matrix)

### Variant 2 ###

current_lst = [[int(n) for n in input().split(", ")] for _ in range(int(input()))]
result = [number for sublist in current_lst for number in sublist]
print(result)