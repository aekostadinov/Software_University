fires_with_their_cells = input().split("#")
amount_of_water = int(input())
efforts = 0
total_fire = []

for index in range(len(fires_with_their_cells)):
    lst_of_fires = fires_with_their_cells[index].split(" = ")
    if lst_of_fires[0] == 'High' and 81 <= int(lst_of_fires[1]) <= 125:
        if amount_of_water >= int(lst_of_fires[1]):
            amount_of_water -= int(lst_of_fires[1])
            total_fire.append(lst_of_fires[1])
            efforts += 0.25 * int(lst_of_fires[1])
    elif lst_of_fires[0] == 'Medium' and 51 <= int(lst_of_fires[1]) <= 80:
        if amount_of_water >= int(lst_of_fires[1]):
            amount_of_water -= int(lst_of_fires[1])
            total_fire.append(lst_of_fires[1])
            efforts += 0.25 * int(lst_of_fires[1])
    elif lst_of_fires[0] == 'Low' and 1 <= int(lst_of_fires[1]) <= 50:
        if amount_of_water >= int(lst_of_fires[1]):
            amount_of_water -= int(lst_of_fires[1])
            total_fire.append(lst_of_fires[1])
            efforts += 0.25 * int(lst_of_fires[1])

print('Cells:')
for i in range(len(total_fire)):
    print(f" - {total_fire[i]}")
print(f"Effort: {efforts:.2f}")
print(f"Total Fire: {sum(list(map(int,total_fire)))}")

