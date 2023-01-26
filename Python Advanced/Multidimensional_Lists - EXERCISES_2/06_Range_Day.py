"""You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated
by a single space:
    · Your position is marked with the symbol "A"
    · Targets marked with symbol "x"
    · All of the empty positions will be marked with "."

After the field state, you will be given an integer representing the number of commands you will receive.
The possible commands are:

    · "move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only
move if the field you want to step on is marked with ".".
    · "shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).
Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot
only the nearest target. When you have shot a target, the field becomes empty position (".").

Validate the positions since they can be outside the field.
Keep track of all the shot targets:

    · If at any point there are no targets left, end the program and print: "Training completed! All {count_targets}
targets hit.".
    · If, after you perform all the commands, there are some targets left print: "Training not completed!
{count_left_targets} targets left.".
Finally, print the index positions of the targets that you hit, as shown in the examples.

Input
    · 5 lines representing the field (symbols, separated by a single space)
    · N - count of commands
    · On the following N lines - the commands in the format described above
Output
    · On the first line, print one of the following:
        o If all the targets were shot
"Training completed! All {count_targets} targets hit."
        o Otherwise:
"Training not completed! {count_left_targets} targets left."
    · Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples."""

matrix = []
player_position = []

total_targets = 0
shooted_targets = 0
targets_positions = []

positions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(5):
    matrix.append(input().split())
    if "A" in matrix[row]:
        player_position = [row, matrix[row].index("A")]
        matrix[row][player_position[1]] = '.'
    if 'x' in matrix[row]:
        total_targets += matrix[row].count("x")

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "move":
        its_move = True
        direction, steps = command[1], int(command[2])
        current_row, current_col = player_position[0], player_position[1]
        for _ in range(steps):
            current_row += positions[direction][0]
            current_col += positions[direction][1]
            if not (0 <= current_row < 5 and 0 <= current_col < 5):
                its_move = False
                break
        else:
            if not matrix[current_row][current_col] == 'x':
                player_position[0], player_position[1] = current_row, current_col

    elif command[0] == "shoot":
        direction = command[1]
        row, col = player_position[0] + positions[direction][0], \
                   player_position[1] + positions[direction][1]
        while True:
            if not (0 <= row < 5 and 0 <= col < 5):
                break
            if matrix[row][col] == 'x':
                total_targets -= 1
                shooted_targets += 1
                matrix[row][col] = '.'
                targets_positions.append([row, col])
                break
            row += positions[direction][0]
            col += positions[direction][1]
        if total_targets == 0:
            break
if total_targets == 0:
    print(f"Training completed! All {shooted_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets} targets left.")
[print(row) for row in targets_positions]

## Variant 2 ###


#
# def move(direction, steps):
#     r = my_position[0] + (directions[direction][0] * steps)
#     c = my_position[1] + (directions[direction][1] * steps)
#
#     if not (0 <= r < size and 0 <= c < size):
#         return my_position
#     if field[r][c] == 'x':
#         return my_position
#
#     return [r, c]
#
#
# def shoot(direction):
#     r = my_position[0] + directions[direction][0]
#     c = my_position[1] + directions[direction][1]
#
#     while 0 <= r < size and 0 <= c < size:
#         if field[r][c] == 'x':
#             field[r][c] = '.'
#             return [r, c]
#
#         r += directions[direction][0]
#         c += directions[direction][1]
#
#
# size = 5
# field = []
#
# targets = 0
# targets_hit = 0
# targets_hit_positions = []
#
# my_position = []
#
# directions = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1),
# }
#
# for row in range(size):
#     field.append(input().split())
#
#     if 'A' in field[row]:
#         my_position = [row, field[row].index('A')]
#         field[row][my_position[1]] = '.'
#     if 'x' in field[row]:
#         targets += field[row].count('x')
#
# for _ in range(int(input())):
#     command_info = input().split()
#
#     if command_info[0] == 'move':
#         my_position = move(command_info[1], int(command_info[2]))
#     elif command_info[0] == 'shoot':
#         target_down_pos = shoot(command_info[1])
#
#         if target_down_pos:
#             targets_hit_positions.append(target_down_pos)
#             targets_hit += 1
#
#         if targets_hit == targets:
#             print(f'Training completed! All {targets} targets hit.')
#             break
#
# if targets_hit < targets:
#     print(f'Training not completed! {targets - targets_hit} targets left.')
#
# [print(target_pos) for target_pos in targets_hit_positions]