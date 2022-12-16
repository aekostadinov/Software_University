"""You will be given a square matrix of integers, each integer separated by a single space, and each row will be on a
new line. On the last line of input, you will receive indexes - coordinates of several cells separated by a single
space,in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
On those cells, there are bombs. You must detonate every bomb in the order they were given. When a bomb explodes,
it deals damage equal to its integer value to all the cells around it (in every direction and in all diagonals).
One bomb can't explode more than once, and after it does, its value becomes 0. When a cell's value reaches 0 or below,
it dies. Dead cells can't explode.You must print the count of all alive cells and their sum. Afterward, print the
matrix with all its cells (including the dead ones).

Input
    *On the first line, you are given the integer N - the size of the square matrix.
    *The following N lines hold each column's values - N numbers separated by a space.
    *On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
Output
    *On the first line, you need to print the count of all alive cells in the format:
"Alive cells: {alive_cells}"
    *On the second line, you need to print the sum of all alive cells in the format:
"Sum: {sum_of_cells}"
    *In the end, print the matrix. A space must separate the cells."""

size = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(size)]
index_information = input().split()
alive_cells = 0
for element in index_information:
    r_index, c_index = (int(index) for index in element.split(","))
    if matrix[r_index][c_index] > 0:
        explode_value = matrix[r_index][c_index]
        for r in range(r_index - 1, r_index + 2):
            for c in range(c_index - 1, c_index + 2):
                if r in range(size) and c in range(size):
                    if matrix[r][c] > 0:
                        matrix[r][c] -= explode_value
sum_of_alive_cells = 0
for r in range(size):
    for c in range(size):
        if matrix[r][c] > 0:
            alive_cells += 1
            sum_of_alive_cells += matrix[r][c]
print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_alive_cells}")
for row in range(size):
    print(' '.join(str(number) for number in matrix[row]))



