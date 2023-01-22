"""Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in the examples below.
    -Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
    -Columns + rows define the middle letter:
        *  column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
        *  column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
Input
    * The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
    * r and c are integers in the range [1, 26]"""
#
# row, column = (int(ent) for ent in input().split())
# matrix = [['' for _ in range(column)] for _ in range(row)]
# for r in range(row):
#     for c in range(column):
#         current_string = chr(97 + r) + chr(97 + r + c) + chr(97 + r)
#         matrix[r][c] += current_string
#     print(' '.join(str for str in matrix[r]))

### Variant 2 ###

row, column = [int(x) for x in input().split()]
matrix = [[f"{chr(97+r)}{chr(97+r+c)}{chr(97+c)}" for c in range(column)] for r in range(row)]
[print(*row) for row in matrix]