"""On the first line, you will be given an integer N, which represents the size of a square matrix. On the second line
you will receive the racing number of the tracked race car.On the next N lines you will be given the rows of  the matrix
(string sequences, separated by whitespace), which will be representing the race route. The tracked race car always
starts with coordinates [0, 0]. Thеre will be a tunnel somewhere across the race route. If the race car runs into the
tunnel , the car goes through it and exits at the other end. There will be always two positions marked with "T"(tunnel).
The finish line will be marked with "F". All other positions will be marked with ".".Keep track of the kilometers passed.
Every time the race car receives a direction and moves to the next position of the race route, it covers 10 kilometers.
If the car goes through the tunnel, it covers NOT 10, but 30 kilometers.On each line, after the matrix is given,
you will be receiving the directions for the race car.
    -left
    -right
    -up
    -down
The race car starts moving across the race route:
    -If you receive "End" command, before the race car manages to reach the finish line, the car is disqualified and
the following output should be printed on the Console: "Racing car {racing number} DNF."
    -If the race car comes across a position marked with ".". The car passes 10 kilometers for the current move and
waits for the next direction.
    -If the race car comes across a position marked with "T" this is the tunnel. The race car goes through it and moves
to the other position marked with  "T" (the other end of the tunnel). The car passes 30 kilometers for the current move.
The tunnel stays behind the car, so the race route is clear, and both the positions marked with "T", should be marked
with ".".
    -If the car reaches the finish line - "F" position, the race is over. The tracked race car manages to finish the
stage and the following output should be printed on the Console: "Racing car {racing number} finished the stage!".
Don’t forget that the car has covered another 10 km with the last move.

Input
    -On the first line you will receive N - the size of the square matrix (race route)
    -On the second line you will receive the racing number of the tracked car
    -On the next N lines, you will receive the race route (elements will be separated by a space).
    -On the following lines, you will receive directions (left, right, up, down).
    -On the last line, you will receive the command "End".

Output
    -If the racing car has reached the finish line before the "End" command is given, print on the Console: "Racing car
{racing number} finished the stage!"
    -If the "End"  command is given and the racing car has not reached the finish line yet, the race ends and the
following message is printed on the Console: "Racing car {racing number} DNF."
    -On the second line, print the distance that the tracked race car has covered: "Distance covered
{kilometers passed} km."
    -At the end, mark the last known position of the race car with "C" and print the final state of the matrix
(race route). The row elements in the output matrix should NOT be separated by a whitespace."""




size_matrix = int(input())
car_number = input()
matrix = []
total_km_passed = 0
car_coordinates = [0, 0]

for _ in range(size_matrix):
    matrix.append(input().split())


def find_end_of_dune(mx):
    for row in range(len(mx)):
        for col in range(len(mx[row])):
            if mx[row][col] == "T":
                return row, col


while True:
    command = input()
    if command == 'End':
        matrix[car_coordinates[0]][car_coordinates[1]] = "C"
        print(f"Racing car {car_number} DNF.")
        break
    elif command == "left":
        car_coordinates[1] -= 1
    elif command == "right":
        car_coordinates[1] += 1
    elif command == "up":
        car_coordinates[0] -= 1
    elif command == "down":
        car_coordinates[0] += 1
    if matrix[car_coordinates[0]][car_coordinates[1]] == "F":
        total_km_passed += 10
        matrix[car_coordinates[0]][car_coordinates[1]] = "C"
        print(f"Racing car {car_number} finished the stage!")
        break
    elif matrix[car_coordinates[0]][car_coordinates[1]] == "T":
        total_km_passed += 30
        matrix[car_coordinates[0]][car_coordinates[1]] = "."
        car_coordinates[0], car_coordinates[1] = find_end_of_dune(matrix)
        matrix[car_coordinates[0]][car_coordinates[1]] = "."
    else:
        total_km_passed += 10

print(f"Distance covered {total_km_passed} km.")
for row in range(len(matrix)):
    print("".join(matrix[row]))
