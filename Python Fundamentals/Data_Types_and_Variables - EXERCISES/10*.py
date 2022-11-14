lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_price = 0
number_of_time_shield_brakes = 0

for game in range(1,lost_fights_count +1):
    if game % 2 == 0:
        total_price += helmet_price
    if game % 3 == 0:
        total_price += sword_price
        if game % 2 == 0:
            total_price += shield_price
            number_of_time_shield_brakes += 1
            if number_of_time_shield_brakes % 2 == 0:
                total_price += armor_price
print(f"Gladiator expenses: {total_price:.2f} aureus")

