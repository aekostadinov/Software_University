"""Write a program that reads a matrix from the console and performs certain operations with its elements.
User input is provided similarly to the problems above - first, you read the dimensions and then the data.
Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1")
and ("row2", "col2") are the coordinates of two points in the matrix. A valid command starts with the "swap" keyword
along with four valid coordinates (no more, no less), separated by a single space.

        *If the command is valid, you should swap the values at the given indexes and print the matrix at each step
(thus, you will be able to check if the operation was performed correctly).
        *If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or
the given coordinates are not valid), print "Invalid input!" and move on to the following command. A negative value
makes the coordinates not valid.

Your program should finish when the command "END" is entered."""

### Variant 1 ###
# row, column = (int(ent) for ent in input().split())
# matrix = [[element for element in input().split()] for _ in range(row)]
#
# command = input()
# while not command == 'END':
#     is_valid = True
#     command_line, *coordinates = command.split()
#     if not command_line == 'swap' or not len(coordinates) == 4:
#         is_valid = False
#     if is_valid:
#         r_1, c_1, r_2, c_2 = (int(index) for index in coordinates)
#         if not (r_1 in range(row) and r_2 in range(row) and c_1 in range(column) and c_2 in range(column)):
#             is_valid = False
#         if is_valid:
#             matrix[r_1][c_1], matrix[r_2][c_2] = matrix[r_2][c_2], matrix[r_1][c_1]
#             for r in range(row):
#                 print(' '.join(str(element) for element in matrix[r]))
#     if not is_valid:
#         print("Invalid input!")
#     command = input()


### Variant 2###

def valid_indexes(indexes):
    if set(indexes[:2]).issubset(valid_rows) and set(indexes[2:]).issubset(valid_columns):
        return True
    return False

def swap_command(command,indexes):
    if command == 'swap' and len(indexes) == 4 and valid_indexes(indexes):
        row1, col1, row2, col2 = indexes
        matrix[row1][col1],matrix[row2][col2] = matrix[row2][col2],matrix[row1][col1]
        print(*[' '.join(matrix[r]) for r in range(rows)], sep="\n")
    else:
        print("Invalid input!")



rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]
print(matrix)

valid_rows = range(rows)
valid_columns = range(columns)

while True:
    command, *info = [int(x) if x.isdigit() else x for x in input().split()]
    if command == 'END':
        break
    swap_command(command,info)
