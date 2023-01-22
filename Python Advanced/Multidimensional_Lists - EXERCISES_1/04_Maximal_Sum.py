"""Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of
its elements. There will be no case with two or more 3x3 squares with equal maximal sum.

Input
   -On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the
range [1, 20]
   -On the following lines, you will receive each row with its columns - integers, separated by a single space
in the range [-20, 20]

Output
   -On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
   -On the following 3 lines, print each element of the found submatrix, separated by a single space"""

# row, column = (int(ent) for ent in input().split())
# matrix = [[int(num) for num in input().split()] for _ in range(row)]
# sum_of_3x3 = 0
# final_matrix = []
# for r in range(row - 2):
#     for c in range(column - 2):
#         current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] \
#                       + matrix[r + 1][c] + matrix[r + 1][c + 1] + matrix[r + 1][c + 2]\
#                       + matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
#         if current_sum >= sum_of_3x3:
#             sum_of_3x3 = current_sum
#             final_matrix = [[matrix[r][c], matrix[r][c + 1], matrix[r][c + 2]],
#                             [matrix[r + 1][c],matrix[r + 1][c + 1],matrix[r + 1][c + 2]],
#                             [matrix[r + 2][c],matrix[r + 2][c + 1],matrix[r + 2][c + 2]]]
# print(f"Sum = {sum_of_3x3}")
# for r in range(3):
#     for c in range(3):
#         print(final_matrix[r][c],end=" ")
#     print()

### Variant 2 ###

rows, column = [int(x) for x in input().split()]
matrix = [[int(num) for num in input().split()] for _ in range(rows)]

max_sum = float("-inf")
biggest_matrix = []

for r in range(rows - 2):
    for c in range(column - 2):
        first_row = matrix[r][c:c+3]
        second_row = matrix[r+1][c:c+3]
        third_row = matrix[r+2][c:c+3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > max_sum:
            max_sum = current_sum
            biggest_matrix = [first_row, second_row, third_row]

print(f"Sum = {sum_of_3x3}")
[print(*biggest_matrix[row]) for row in range(3)]

