"""You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n
lines, you will receive the rows of the territory:
    · Alice will be placed in a random position, marked with the letter "A".
    · On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position, she
collects the tea bags and increases the quantity with the corresponding number.
    · There will always be one rabbit hole on the territory marked with the letter "R".
    · All of the empty positions will be marked with ".".

After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or
"right".

When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue
collecting. Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program
ends.
In the end, the path she walked had to be marked with '*'.
For more clarifications, see the examples below.

Input
    · On the first line, you will be given the integer n – the size of the square matrix
    · On the following n lines - matrix representing the field (each position separated by a single space)
    · On each of the following lines, you will be given a move command

Output
    · On the first line:
        o If Alice steps on the rabbit hole or she go out of the territory, print:
        "Alice didn't make it to the tea party."
        o If she collected at least 10 bags of tea, print:
        "She did it! She went to the party."
    · On the following lines, print the matrix."""

size = int(input())

matrix = [input().split() for _ in range(size)]
allice_position = []
collected_teas = 0

positions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    if "A" in matrix[row]:
        allice_position = [row, matrix[row].index("A")]
        matrix[allice_position[0]][allice_position[1]] = "*"

command = input()
its_find = False
while command:
    r_step, c_step = positions[command]
    r, c = r_step + allice_position[0], c_step + allice_position[1]
    if not (0 <= r < size and 0 <= c < size):
        break
    position = matrix[r][c]
    matrix[r][c] = "*"
    if position == "R":
        break
    if position.isdigit():
        collected_teas += int(position)
    if collected_teas >= 10:
        its_find = True
        break
    allice_position[0], allice_position[1] = r, c
    command = input()
if its_find:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*matrix[row]) for row in range(size)]