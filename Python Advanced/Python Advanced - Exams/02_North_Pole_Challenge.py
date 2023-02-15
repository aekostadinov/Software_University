"""You will be given the size of the matrix in the format "{rows}, {columns}". It is the Santa's workshop represented
as some symbols separated by a single space:
    -Your position is marked with the symbol "Y"
    -Christmas decorations are marked with the symbol "D"
    -Gifts are marked with the symbol "G"
    -Cookies are marked with the symbol "C"
    -All of the empty positions will be marked with "."
After the field state, you will be given commands until you receive the command "End". The commands will be in the
format "right/left/up/down-{steps}". You should move in the given direction with the given steps and collect all the
items that come across. If you go out of the field, you should continue to traverse the field from the opposite side in
the same direction. You should mark your path with "x". Your current position should always be marked with "Y".
Keep track of all collected items. If you've collected all items at any point, end the program and print: "Merry
Christmas!".

Input
    -On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
    -On the next lines, you will receive each row with its columns - symbols, separated by a single space.
    -On the following lines, you will receive commands in the format described above until you receive the command
"End" or until you collect all items.

Output
    -On the first line, if you have collected all items, print:
        o"Merry Christmas!"
        oOtherwise, skip the line
    -Next, print the number of collected items in the format:
        o"You've collected:
        o- {number_of_decoration} Christmas decorations
        o- {number_of_gifts} Gifts
        o- {number_of_cookies} Cookies"
    -Finally, print the field, as shown in the examples."""


def my_positions():
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 'Y':
                return r, c


def items():
    collected_items = {"D": 0, "G": 0, "C": 0}
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == "D":
                collected_items["D"] += 1
            elif matrix[r][c] == "G":
                collected_items["G"] += 1
            elif matrix[r][c] == "C":
                collected_items["C"] += 1
    return collected_items


def check_moves(r, c):
    if r >= rows:
        r -= rows
    elif r < 0:
        r = rows + r
    elif c >= columns:
        c -= columns
    elif c < 0:
        c = columns + c
    return r, c


rows, columns = list(map(int, input().split(", ")))

matrix = [[element for element in input().split()] for _ in range(rows)]
command = input()
directions = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}
my_position_r, my_position_c = my_positions()
number_decorations = 0
number_gifts = 0
number_cookies = 0
while not command == 'End':
    direction, steps = [int(el) if el.isdigit() else el for el in command.split("-")]
    all_items = items()
    for _ in range(steps):
        step_r, step_c = directions[direction]
        current_r, current_c = step_r + my_position_r, step_c + my_position_c
        r, c = check_moves(current_r, current_c)
        if matrix[r][c] == 'D':
            number_decorations += 1
            all_items['D'] -= 1
        elif matrix[r][c] == 'G':
            number_gifts += 1
            all_items['G'] -= 1
        elif matrix[r][c] == 'C':
            number_cookies += 1
            all_items['C'] -= 1
        matrix[my_position_r][my_position_c] = "x"
        my_position_r, my_position_c = r, c
        if sum(all_items.values()) == 0:
            break
    matrix[my_position_r][my_position_c] = "Y"
    if sum(all_items.values()) == 0:
        print("Merry Christmas!")
        break
    command = input()
print(f"You've collected:\n- {number_decorations} Christmas decorations\n- {number_gifts} Gifts\n- {number_cookies} Cookies")
for row in matrix:
    print(' '.join(row))
