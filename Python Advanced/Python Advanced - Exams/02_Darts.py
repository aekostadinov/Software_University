"""You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:
1	2	3	4	5	6	7
24	D	D	D	D	D	8
23	D	T	T	T	D	9
22	D	T	B	T	D	10
21	D	T	T	T	D	11
20	D	D	D	D	D	12
19	18	17	16	15	14	13

Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player.
The score for each turn is deducted from the player’s total score. The first player who reduces their score to zero
or less wins the game.
You are going to receive the information for every throw on a separate line. The coordinate information of a hit will
be in the format: "({row}, {column})".
    -If a player hits outside the dartboard, he does not score any points.
    -If a player hits a number, it is deducted from his total.
    -If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled and then deducted
from his total.
    -If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and then deducted
from his total.
    -"B" is the bullseye. If a player hits it, he wins the game, and the program ends.
For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are
deducted from his total.
Your job is to find who won the game and with how many turns.

Input
    -The name of the first player and the name of the second player, separated by ", "
    -7 lines – the dartboard (separated by single space)
    -On the next lines - the coordinates in the format: "({row}, {column})"

Output
    -You should print only one line containing the winner and his count of throws:
"{name} won the game with {count_turns} throws!"""


first_player, second_player = input().split(", ")
matrix = [[int(num) if num.isdigit() else num for num in input().split()] for _ in range(7)]
player_points = {first_player: 501, second_player: 501}
player_turns = {first_player: 0, second_player: 0}
counter = 1
while True:
    points = 0
    if counter % 2 == 1:
        current_player = first_player
        player_turns[first_player] += 1
    else:
        current_player = second_player
        player_turns[second_player] += 1
    row, column = [int(num) for num in input().strip("(").strip(")").split(", ")]
    if row not in range(7) or column not in range(7):
        counter += 1
        continue
    if matrix[row][column] == "B":
        print(f"{current_player} won the game with {player_turns[current_player]} throws!")
        break
    elif matrix[row][column] == "D":
        points = 2 * (matrix[row][0] + matrix[row][6] + matrix[0][column] + matrix[6][column])
    elif matrix[row][column] == "T":
        points = 3 * (matrix[row][0] + matrix[row][6] + matrix[0][column] + matrix[6][column])
    else:
        points = matrix[row][column]
    player_points[current_player] -= points
    if player_points[current_player] <= 0:
        print(f"{current_player} won the game with {player_turns[current_player]} throws!")
        break
    counter += 1
