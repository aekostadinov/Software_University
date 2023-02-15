"""You will be given a matrix with 6 rows and 6 columns representing the board. On the board, there will be points
(integers) and buckets marked with the letter "B". Rules of the game:
    -You can throw a ball only 3 times.
    -When you hit a bucket (position marked with 'B'), you score the sum of the points in the same column.
    -You can hit a bucket only once. If you hit the same bucket again, you do not score any points.
    -If you hit outside a bucket (hit a number on the board) or outside the board, you do not score any points.
After the board state, you are going to receive the information for every throw on a separate line. The coordinates’
information of a hit will be in the format: "({row}, {column})".
Depending on how many points you have collected, you win one of the following:

Football	                100 to 199 points
Teddy Bear	                200 to 299 points
Lego Construction Set	    300 and more points

Your job is to keep track of the scored points and to check if you won a prize.
For more clarifications, see the examples below.

Input
    -6 lines – matrix representing the board (each position separated by a single space)
    -On the next 3 lines - the coordinates of the throw in the format: "({row}, {column})"

Output
    On the first line:
        oIf you won a prize, print:
"Good job! You scored {points} points, and you've won {prize}."
        oIf you did not win any prize, print the points you need to get at least the first prize:
"Sorry! You need {points} points more to win a prize."""

matrix = [[int(num) if num.isdigit() else num for num in input().split()] for _ in range(6)]
total_points = 0
bucket_indexes = []
for _ in range(3):
    row, column = [int(num) for num in input().strip("(").strip(")").split(", ")]
    if row not in range(6) or column not in range(6):
        continue
    if matrix[row][column] == "B" and ((row, column) not in bucket_indexes):
        bucket_indexes.append((row, column))
        for index in range(6):
            if matrix[index][column] != "B":
                total_points += matrix[index][column]
if total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
else:
    if 100 <= total_points <= 199:
        print(f"Good job! You scored {total_points} points, and you've won Football.")
    elif 200 <= total_points <= 299:
        print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
    elif 300 <= total_points:
        print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
