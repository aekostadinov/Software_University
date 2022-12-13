"""Write a program that reads a matrix from the console and prints:
    - The sum of all numbers in matrix
    - The matrix itself
On the first line you will receive the matrix sizes in the format "{rows}, {columns}".On the
next rows ,you will get elements for each column separated by a comma and a space", ". """

rows, columns = map(int,input().split(", "))
matrix_of_numbers = []

for _ in range(rows):
    current_matrix = [int(x) for x in input().split(", ")]
    matrix_of_numbers.append(current_matrix)

print(sum(sum(row) for row in matrix_of_numbers))
print(matrix_of_numbers)


### Variant 2 ###

# rows, columns = map(int,input().split(", "))
# matrix_of_numbers = []
# matrix_sum = 0
#
# for _ in range(rows):
#     current_matrix = [int(x) for x in input().split(", ")]
#     matrix_of_numbers.append(current_matrix)
#     for index in range(columns):
#         matrix_sum += current_matrix[index]
# print(matrix_sum)
# print(matrix_of_numbers)