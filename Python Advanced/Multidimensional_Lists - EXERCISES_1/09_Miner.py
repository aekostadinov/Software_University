"""First, you will receive the size of a square field in which the miner should move.
On the second line, you will receive the commands for the miner's movement, separated by a single space.
The possible commands are "left", "right", "up" and "down".In the end, you will receive each row of the
field on a separate line. The possible characters that may appear on the screen are:
    - * - a regular position on the field
    - e - the end of the route
    - c - coal
    - s - miner
The miner starts moving from the position "s". He should perform the given commands successively, moving with only
one position in the given direction. If the miner has reached the edge of the field and the following command indicates
that he has to get out of the area, he must remain in his current position and ignore the command.When the miner finds
coal, he collects it and replaces it with "*". Keep track of the collected coal. In the end, you should print whether
the miner has succeeded in collecting the coal or not and his final position:
    - If the miner has collected all coal in the field, the program stops, and you should print the message:
"You collected all coal! ({row_index}, {col_index})".
    - If the miner steps at "e", the game is over (the program stops), and you should print the message:
"Game over! ({row_index}, {col_index})".
    - If there are no more commands and none of the above cases had happened, you should print the message:
"{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".

Input
    -Field size - an integer number
    -Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
    -The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")

Output
    -There are three types of output as mentioned above."""

def find_started_index():
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 's':
                return r, c


def checked_indexes(r, c):
    if r in range(size) and c in range(size):
        return True


def all_coals():
    number_of_coals = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'c':
                number_of_coals += 1
    return number_of_coals

size = int(input())
directions = input().split()
matrix = [[char for char in input().split()] for _ in range(size)]
start_r, start_c = find_started_index()
all_coals = all_coals()
is_end = False
for direction in directions:
    if direction == 'up':
        if checked_indexes(start_r - 1, start_c):
            start_r -= 1
    elif direction == 'down':
        if checked_indexes(start_r + 1, start_c):
            start_r += 1
    elif direction == 'left':
        if checked_indexes(start_r, start_c - 1):
            start_c -= 1
    elif direction == 'right':
        if checked_indexes(start_r, start_c + 1):
            start_c += 1
    current_symbol = matrix[start_r][start_c]
    if current_symbol == 'e':
        print(f"Game over! ({start_r}, {start_c})")
        is_end = True
        break
    elif current_symbol == 'c':
        all_coals -= 1
        matrix[start_r][start_c] = '*'
        if all_coals == 0:
            print(f"You collected all coal! ({start_r}, {start_c})")
            break
if all_coals > 0 and not is_end:
    print(f"{all_coals} pieces of coal left. ({start_r}, {start_c})")


