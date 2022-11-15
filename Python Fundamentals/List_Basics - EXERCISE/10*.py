initial_energy = 100
initial_coins = 100
working_days_events = input().split('|')
for index in range(len(working_days_events)):
    current_day_event = working_days_events[index].split("-")
    first_part = current_day_event[0]
    second_part = int(current_day_event[1])
    if first_part == 'rest':
        if initial_energy + second_part <= 100:
            gained_energy = second_part
            initial_energy += gained_energy
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {initial_energy}.")
        else:
            gained_energy = 100 - initial_energy
            initial_energy += gained_energy
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {initial_energy}.")
    elif first_part == 'order':
        if initial_energy >= 30:
            initial_coins += second_part
            initial_energy -= 30
            earned_coins = second_part
            print(f"You earned {earned_coins} coins.")
        else:
            print("You had to rest!")
            if (initial_energy + 50) >= 100:
                initial_energy = 100
            else:
                initial_energy += 50
    else:
        ingredient = first_part
        price_for_ingredient = second_part
        if initial_coins >= price_for_ingredient:
            initial_coins -= price_for_ingredient
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            exit()
print("Day completed!")
print(f"Coins: {initial_coins}")
print(f"Energy: {initial_energy}")







