"""Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will get
elements for each column separated with a single space."""


row, column = map(int, input().split(", "))
matrix = [[int(num) for num in input().split()] for _ in range(row)]
for column_index in range(column):
    current_sum = 0
    for row_index in range(row):
        current_sum += matrix[row_index][column_index]
    print(current_sum)
