"""First, you will receive a line holding integers N and M, representing the lair's rows and columns.
Next, you receive N strings that can consist only of ".", "B", "P". They represent the initial state of the lair.
There will be only one player. The bunnies are marked with "B", the player is marked with "P", and everything else
is free space, marked with a dot ".". Then you will receive a string with commands (e.g., LRRULUD) - each letter
represents the next move of the player:
    -L - the player should move one position to the left
    -R - the player should move one position to the right
    -U - the player should move one position up
    -D - the player should move one position down
After every step made, each bunny spreads one position up, down, left, and right. If the player moves to a bunny
cell or a bunny reaches the player, the player dies. If the player goes out of the lair without encountering a bunny,
the player wins.When the player dies or wins, the game ends. All the activities for this turn continue (e.g., all the
bunnies spread normally), but there are no more turns. There will be no cases where the moves of the player end before
he dies or escapes.In the end, print the final state of the lair with every row on a separate line. On the last line,
print either "dead: {row} {col}" or "won: {row} {col}". "Row" and "col" are the cell coordinates where the player has
died or the last cell he has been in before escaping the lair.

Input
    -On the first line of input, the numbers N and M are received - the number of rows and columns in the lair
    -On the following N lines, each row is received in the form of a string. The string will contain only ".", "B", "P".
All strings will be the same length. There will be only one "P" for all the input
    -On the last line, the directions are received in the form of a string, containing "R", "L", "U", "D"

Output
    -On the first N lines, print the final state of the bunny lair
    -On the last line, print:
        oIf the player won - "won: {row} {col}"
        oIf the player dies - "dead: {row} {col}"""



def check_player(row, column):
    for r in range(row):
        for c in range(column):
            if matrix[r][c] == 'P':
                return r, c


def check_bunny(row, column):
    indexes = []
    for r in range(row):
        for c in range(column):
            if matrix[r][c] == 'B':
                if (r, c) not in indexes:
                    indexes.append((r, c))
    return indexes


def player_moves(row, column):
    its_dead = False
    if matrix[row][column] == 'B':
        its_dead = True
    else:
        matrix[row][column] = 'P'
    matrix[player_r][player_c] = '.'
    return its_dead


def check_indexes(row, column):
    if 0 <= row < r and 0 <= column < c:
        return True


def check_bunny_moves(row, column):
    its_dead = False
    for moves in possible_positions.values():
        current_bunny_r = row + moves[0]
        current_bunny_c = column + moves[1]
        if 0 <= current_bunny_r < r and 0 <= current_bunny_c < c:
            if matrix[current_bunny_r][current_bunny_c] == 'P':
                its_dead = True
            matrix[current_bunny_r][current_bunny_c] = 'B'
    return its_dead


r, c = map(int, input().split())
matrix = [[char for char in input()] for _ in range(r)]
command = input()
possible_positions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
its_dead, its_win = False, False
player_r, player_c = check_player(r, c)
for char in command:
    step_r, step_c = possible_positions[char]
    current_player_r, current_player_c = step_r + player_r, step_c + player_c
    if check_indexes(current_player_r, current_player_c):
        if player_moves(current_player_r, current_player_c):
            its_dead = True
        player_r, player_c = current_player_r, current_player_c
    else:
        its_win = True
        matrix[player_r][player_c] = '.'
    for indexes in check_bunny(r, c):
        bunny_r, bunny_c = indexes
        if check_bunny_moves(bunny_r, bunny_c):
            its_dead = True
    if its_dead or its_win:
        break
for lists in matrix:
    print(''.join(lists))
if its_win:
    print(f"won: {player_r} {player_c}")
elif its_dead:
    print(f"dead: {player_r} {player_c}")


