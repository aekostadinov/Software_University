"""First, you will be given a sequence of integers representing firework effects. Afterwards you will be given another
sequence of integers representing explosive power.You need to start from the first firework effect and try to mix it
with the last explosive power. If the sum of their values is:
    -divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
    -divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
    -divisible by both 3 and 5 – create Crossette firework and remove both materials
Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence. Then, try to mix the
same explosive power with the next firework effect.
If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other.
When you have successfully prepared enough fireworks for the show or you have no more firework punches or explosive
power, you need to stop mixing.
To make the perfect firework show, Maria needs 3 of each of the firework types.

Input
    -On the first line, you will receive the integers representing the firework effects, separated by ", ".
    -On the second line, you will receive the integers representing the explosive power, separated by ", ".

Output
    -On the first line, print:
        oif Maria successfully prepared the firework show: "Congrats! You made the perfect firework show!"
        oif Maria failed to prepare it: "Sorry. You can't make the perfect firework show."
    -On the second line, print all firework effects left if there are any:
        o"Firework Effects left: {effect1}, {effect2}, (…)"
    -On the third line, print all explosive fillings left if there are any:
        o" Explosive Power left: {filling1}, {filling2}, (…)"
    -Then, you need to print all fireworks and the amount you have of them:
        o"Palm Fireworks: {count}"
        o"Willow Fireworks: {count}"
"Crossette Fireworks: {count}"""

from collections import deque

fireworks_effects = deque(int(num) for num in input().split(", "))  # first
explosive_power = deque(int(num) for num in input().split(", "))  # last
type_of_fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
successfully_prepared = False

while fireworks_effects and explosive_power:
    current_firework = fireworks_effects[0]
    current_power = explosive_power[-1]
    if current_firework <= 0:
        fireworks_effects.popleft()
        continue
    if current_power <= 0:
        explosive_power.pop()
        continue
    sum_of_values = current_power + current_firework
    if sum_of_values % 3 == 0 and sum_of_values % 5 != 0:
        type_of_fireworks["Palm Fireworks"] += 1
        explosive_power.pop()
    elif sum_of_values % 5 == 0 and sum_of_values % 3 != 0:
        type_of_fireworks["Willow Fireworks"] += 1
        explosive_power.pop()
    elif sum_of_values % 3 == 0 and sum_of_values % 5 == 0:
        type_of_fireworks["Crossette Fireworks"] += 1
        explosive_power.pop()
    else:
        current_firework -= 1
        fireworks_effects.append(current_firework)
    fireworks_effects.popleft()
    if all(value >= 3 for value in type_of_fireworks.values()):
        successfully_prepared = True
        break
if successfully_prepared:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fireworks_effects:
    print(f"Firework Effects left: {', '.join(str(el) for el in fireworks_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(el) for el in explosive_power)}")
print(f"Palm Fireworks: {type_of_fireworks['Palm Fireworks']}\nWillow Fireworks: \
{type_of_fireworks['Willow Fireworks']}\nCrossette Fireworks: {type_of_fireworks['Crossette Fireworks']}")




