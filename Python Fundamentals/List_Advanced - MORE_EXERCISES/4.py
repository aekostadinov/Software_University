count = int(input())
all_rows = []
number_of_destroyed_ships = 0

for _ in range(count):
    current_row = [int(num) for num in input().split()]
    all_rows.append(current_row)
attacked_information = input().split()

for index in range(len(attacked_information)):
    row, column = attacked_information[index].split("-")
    row = int(row)
    column = int(column)
    if all_rows[row][column] == 0:
        continue
    elif all_rows[row][column] == 1:
        number_of_destroyed_ships += 1
        all_rows[row][column] -= 1
    else:
        all_rows[row][column] -= 1
print(number_of_destroyed_ships)


