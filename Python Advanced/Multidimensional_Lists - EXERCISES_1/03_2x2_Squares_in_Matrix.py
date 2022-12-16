"""Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, you will receive the
matrix's dimensions in the format "{rows} {columns}". On the following rows, you will receive characters separated by
a single space. Print the number of all square matrices you have found."""

row, column = (int(ent) for ent in input().split())
matrix = [[char for char in input().split()] for _ in range(row)]
coincidence = 0
for row_index in range(row - 1):
    for column_index in range(column - 1):
        if matrix[row_index][column_index] == matrix[row_index][column_index + 1] \
                == matrix[row_index + 1][column_index] == matrix[row_index + 1][column_index + 1]:
            coincidence += 1
print(coincidence)
