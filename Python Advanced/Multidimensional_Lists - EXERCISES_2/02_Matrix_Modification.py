"""Write a program that reads a matrix from the console and changes its values. On the first line, you will get
the matrix's rows - N. You will get elements for each column on the following N lines, separated with a single space.
You will be receiving commands in the following format:
    -"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
    -"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given
indexes are in range [0; len() – 1].When you receive "END", you should print the matrix and stop the program."""

def check_indexes(r,c):
    if r in range(size) and c in range(size):
        return True

size = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(size)]
command_line = input()
while not command_line == 'END':
    command, *value_indexes = command_line.split()
    r, c, value = map(int, value_indexes)
    if check_indexes(r,c):
        if command == 'Add':
            matrix[r][c] += value
        elif command == 'Subtract':
            matrix[r][c] -= value
    else:
        print("Invalid coordinates")
    command_line = input()
for r in range(size):
    print(' '.join(str(num) for num in matrix[r]))

