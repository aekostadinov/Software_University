"""Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
On the first line, you will receive an integer N - the size of a square matrix. The following N lines hold the
values for each column - N numbers separated by a single space. Print the absolute difference between the primary
and the secondary diagonal sums."""

size = int(input())
matrix = [input().split() for _ in range(size)]
primary = []
secondary = []
for s in range(size):
    p_num = int(matrix[s][s])
    primary.append(p_num)
    s_num = int(matrix[s][size - s - 1])
    secondary.append(s_num)
abs_difference = abs(sum(primary) - sum(secondary))
print(abs_difference)