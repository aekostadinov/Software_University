"""Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right).
On the first line, you will receive an integer N – the size of a square matrix. The next N lines holds the values for
each column - N numbers, separated by a single space. """

matrix_size = int(input())
sum_of_primary_diagonal_numbers = 0
matrix = [[int(num) for num in input().split()] for _ in range(matrix_size)]
for index in range(matrix_size):
    sum_of_primary_diagonal_numbers += matrix[index][index]
print(sum_of_primary_diagonal_numbers)
