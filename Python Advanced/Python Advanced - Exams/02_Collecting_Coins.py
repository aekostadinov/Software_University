"""On the first line, you will be given a number representing the size of the field with a square shape. On the
following few lines, you will be given the field with:
    -One player - randomly placed in it and marked with the symbol "P"
    -Numbers for coins placed at different positions of the field
    -Walls marked with "X"
After the field state, you will be given commands for the player's movement. Commands can be: "up", "down", "left",
"right". If the command is invalid, you should ignore it.
The player moves in the given direction with one step for each command and collects all the coins that come across.
If he goes out of the field, he should continue to traverse the field from the opposite side in the same direction.
Note: He can go through the same path many times, but he can collect the coins just once (the first time).
There are only two possible outcomes of the game:
    -The player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to the next-lowest number.
    -The player collects at least 100 coins and wins the game.
For more clarifications, see the examples below.

Input
    -A number representing the size of the field (matrix NxN)
    -A matrix representing the field (each position separated by a single space)
    -On each of the following lines, you will get a move command.
Output
    -If the player won the game, print: "You won! You've collected {total_coins} coins."
    -If the player loses the game, print: "Game over! You've collected {total_coins} coins."
    -Collected coins have to be rounded down to the next-lowest number.
    -The player's path as cooridnates in lists on separate lines:
"Your path:
[{row_position1}, {column_position1}]
[{row_position2}, {column_position2}]
…
[{row_positionN}, {column_positionN}]"""


def player_indexes():
    for r in range(size_of_the_field):
        for c in range(size_of_the_field):
            if matrix[r][c] == "P":
                return r, c


def check_indexes(r, c):
    if r >= size_of_the_field:
        r = 0
    elif r < 0:
        r = size_of_the_field - 1
    elif c >= size_of_the_field:
        c = 0
    elif c < 0:
        c = size_of_the_field - 1
    return r, c


size_of_the_field = int(input())
collected_coins = 0
matrix = [[int(num) if num.isdigit() else num for num in input().split()] for _ in range(size_of_the_field)]
player_r, player_c = player_indexes()
my_path = [[player_r,player_c]]
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


while True:
    command = input()
    if command not in directions:
        command = input()
        continue
    current_r, current_c = player_r + directions[command][0], player_c + directions[command][1]
    row, column = check_indexes(current_r, current_c)
    my_path.append([row,column])
    if matrix[row][column] == "X":
        collected_coins = collected_coins // 2
        print(f"Game over! You've collected {collected_coins} coins.")
        break
    elif matrix[row][column] != "P":
        collected_coins += matrix[row][column]
    if collected_coins >= 100:
        print(f"You won! You've collected {collected_coins} coins.")
        break
    matrix[row][column] = "P"
    player_r, player_c = row, column
print(f"Your path:")
for lst in my_path:
    print(lst)


