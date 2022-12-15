"""You are tasked to visualize a snake's zigzag path in a rectangular matrix with a size N x M.
A string represents the snake. It starts moving from the top-left corner to the right. When the snake reaches
the end of the row, it slithers its way down to the next row and turns left. The moves are repeated to the very end.
The first cell is filled with the first symbol of the snake. The second cell is filled with the second symbol, etc.
The snake's path is as long as it takes to fill the matrix completely - if you reach the end of the string representing
the snake, start again at the first symbol. In the end, you should print the snake's path.

Input
The input data consists of exactly two lines:
   *On the first line, you will receive the dimensions N x M of the field in format: "{rows} {columns}".
   *On the second line, you will receive the string representing the snake

Output
   *You should print the snake's zigzag path of size N x M (rows x columns)"""

from collections import deque

def add_char(row,column):
    current_char = console_string.popleft()
    matrix[row][column] += current_char
    console_string.append(current_char)


row, column = (int(ent) for ent in input().split())
matrix = [['' for _ in range(column)] for _ in range(row)]
console_string = deque([char for char in input()])
current_index = 0
for r in range(row):
    if current_index % 2 == 0:
        for c in range(column):
            add_char(r,c)
    else:
        for c in range(column - 1,-1,-1):
            add_char(r,c)
    current_index += 1
for element in matrix:
    print(''.join(char for char in element))