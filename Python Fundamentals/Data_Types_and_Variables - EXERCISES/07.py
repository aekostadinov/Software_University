number_of_lines = int(input())
capacity = 255
water_in_tank = 0

for _ in range(number_of_lines):
    litters_of_water = int(input())
    if capacity >= litters_of_water:
        capacity -= litters_of_water
        water_in_tank += litters_of_water
    else:
        print("Insufficient capacity!")
        continue
print(water_in_tank)


