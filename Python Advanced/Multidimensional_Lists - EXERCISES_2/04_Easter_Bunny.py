"""On the first line, you will be given a number representing the size of the field. On the following few lines,
you will be given a field with:
    -One bunny - randomly placed in it and marked with the symbol "B"
    -Number of eggs placed at different positions of the field and traps marked with "X"
Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
The directions that should be considered as possible are up, down, left, and right. If you reach a trap while
checking some of the directions, you should not consider the fields after the trap in this direction.
For more clarifications, see the examples below.
Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.

Input
    -A number representing the size of the field
    -The matrix representing the field (each position separated by a single space)

Output
    -The direction which should be considered as best (lowercase)
    -The field positions from which we are collecting eggs as lists
    -The total number of eggs collected"""


def check_bunny_positions(size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'B':
                return [r, c]


def check_corridor(bunny_row_index, bunny_column_index):
    for direction, row, column in (("up", -1, 0), ("down", 1, 0), ("left", 0, -1), ("right", 0, 1)):
        bunny_move_r, bunny_move_c, sum, coord = bunny_row_index + row, bunny_column_index + column, 0, []
        for jump in range(size):
            if 0 <= bunny_move_r < size and 0 <= bunny_move_c < size and matrix[bunny_move_r][bunny_move_c] != "X":
                sum += matrix[bunny_move_r][bunny_move_c]
                coord.append([bunny_move_r, bunny_move_c])
                bunny_move_r, bunny_move_c = row + bunny_move_r, column + bunny_move_c
            else:
                result[sum] = {direction: coord}
                break


size = int(input())
matrix = [[int(char) if char[-1].isdigit() else char for char in input().split()] for _ in range(size)]
result = {}
bunny_row_index, bunny_column_index = check_bunny_positions(size)
check_corridor(bunny_row_index, bunny_column_index)
max_sum = max(result)
for direction, paths in result[max_sum].items():
    print(direction)
    for indexes in paths:
        print(indexes)
    print(max_sum)
