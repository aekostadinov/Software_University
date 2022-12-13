"""Write a program that receives a matrix of numbers and prints a new one only with the numbers
that are even.Use nested comprehension for that problem.
On the first line you will receive the rows of the matrix.On the next rows,you will get elements
for each column separated with a comma and a space."""


###Variant 1 ###
rows = int(input())
result = []
for row in range(rows):
    nums = [int(num) for num in input().split(", ")]
    even_nums = [number for number in nums if number % 2 == 0]
    result.append(even_nums)
print(result)


###Variant 2 ###
# rows = int(input())
# even_matrix = []
# matrix = [[int(num) for num in input().split(", ")] for _ in range(rows)]
# for row in matrix:
#     only_even = [x for x in row if x % 2 == 0]
#     even_matrix.append(only_even)
# print(even_matrix)
