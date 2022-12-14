"""Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with biggest
sum of its values. On first line you will get matrix sizes in format "{rows}, {columns}".  On the next rows,
you will get elements for each column, separated with a comma and a space ", ". You should print the found
submatrix and the sum of its elements,as shown in the examples. """

row, column = (int(ent) for ent in input().split(", "))
matrix = [[int(num) for num in input().split(", ")] for _ in range(row)]
sum_of_2x2 = 0
final_matrix = []
for row_index in range(row - 1):
    for column_index in range(column - 1):
        current_sum = matrix[row_index][column_index] + matrix[row_index][column_index + 1] \
                      + matrix[row_index + 1][column_index] + matrix[row_index + 1][column_index + 1]
        if current_sum > sum_of_2x2:
            sum_of_2x2 = current_sum
            final_matrix = [[matrix[row_index][column_index], matrix[row_index][column_index + 1]],
                            [matrix[row_index + 1][column_index],matrix[row_index + 1][column_index + 1]]]
for r in range(2):
    for c in range(2):
        print(final_matrix[r][c],end=" ")
    print()
print(sum_of_2x2)