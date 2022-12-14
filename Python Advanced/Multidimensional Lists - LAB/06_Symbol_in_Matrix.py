"""Write a program that reads a number - N, representing the rows and columns of a square matrix. On the next N lines,
you will receive rows of the matrix. Each row consists of ASCII characters. After that, you will receive a symbol.
Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})".
You should start searching from the top left. If there is no such symbol, print the message "{symbol} does not
occur in the matrix"."""

n = int(input())
matrix = [input() for _ in range(n)]
searched_symbol = input()

is_found = False
for row in range(n):
    for column in range(n):
        if matrix[row][column] == searched_symbol:
            r,c = row, column
            is_found = True
            print((r,c))
            break
    if is_found:
        break
if not is_found:
    print(f"{searched_symbol} does not occur in the matrix")



