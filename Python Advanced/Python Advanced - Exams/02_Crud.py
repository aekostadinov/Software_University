"""In the beginning, you will be given a matrix with 6 rows and 6 columns representing a table with
information.It consists of:
    -Letters - on one or many positions in the table
    -Numbers - on one or many positions in the table
    -Empty positions - marked with "."

Next, you will receive your first position on the table in the format "({row}, {column})"
On the following lines, until you receive "Stop" you will be receiving commands in the format:
    -"Create, {direction}, {value}"
        oThe direction could be "up", "down", "left" or "right"
        oIf you step in an empty position, create the given value on that position. E.g., if the given
value is "A", and the position is empty (".") - change it to "A"
        oIf the position is NOT empty, do NOT create a value on that position
    -"Update, {direction}, {value}"
        oThe direction could be "up", "down", "left" or "right"
        oIf you step on a letter or number, update the position with the given value. E.g., if the given
value is "h", and the position's value is "12" - change it to "h"
        oIf the position is empty, do NOT update the value on that position
    -"Delete, {direction}"
        oThe direction could be "up", "down", "left" or "right"
        oIf you step on a letter or number, delete it, and empty the position. E.g., if the given position's value is "h" - change it to "."
        oIf the position is already empty, do NOT delete it
    -"Read, {direction}"
        oThe direction could be "up", "down", "left" or "right"
        oIf you step on a letter or number, print it on the console
        oIf the position is empty, do NOT read it
You can make only ONE move at a time in the given direction for each command given.
In the end, print the final matrix.

Input
    -On the first 6 lines - a matrix with positions separated by a single space
            oLetters are in the range [a-zA-Z]
            oNumbers are in the range [-100, 100]
    -On the next line - your first position in the format: "({row}, {column})"
    -On the following lines until you receive the command "Stop" - commands in the format shown above

Output
    -In the end, print the final matrix, each row on a new line, each position separated by a single space."""


def check_current_positions(directions):
    if directions == 'up':
        current_positions = [r - 1, c]
    elif directions == 'down':
        current_positions = [r + 1, c]
    elif directions == 'left':
        current_positions = [r, c - 1]
    else:
        current_positions = [r, c + 1]
    row, column = current_positions[0], current_positions[1]
    return (row, column)


matrix = [[int(char) if char.isdigit() else char for char in input().split()] for _ in range(6)]
first_positions = input()
r, c = [int(first_positions[1]), int(first_positions[4])]
data = input()
while not data == 'Stop':
    command_line = data.split(", ")
    command = command_line[0]
    directions = command_line[1]
    if command == 'Create':
        value = command_line[2]
        r, c = check_current_positions(directions)
        if matrix[r][c] == '.':
            matrix[r][c] = value
    elif command == 'Update':
        value = command_line[2]
        r, c = check_current_positions(directions)
        if not matrix[r][c] == ".":
            matrix[r][c] = value
    elif command == 'Delete':
        r, c = check_current_positions(directions)
        if not matrix[r][c] == ".":
            matrix[r][c] = '.'
    elif command == 'Read':
        r, c = check_current_positions(directions)
        if not matrix[r][c] == ".":
            print(matrix[r][c])
    data = input()

for lst in matrix:
    print(' '.join(str(el) for el in lst))


