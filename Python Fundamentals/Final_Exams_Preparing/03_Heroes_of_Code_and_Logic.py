"""On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose for your party. On the next n lines, the heroes themselves will follow with their hit points and mana points separated by a single space in the following format:
"{hero name} {HP} {MP}"
	•	HP stands for hit points and MP for mana points
	•	a hero can have a maximum of 100 HP and 200 MP
After you have successfully picked your heroes, you can start playing the game. You will be receiving different
commands, each on a new line, separated by " – ", until the "End" command is given.
There are several actions that the heroes can perform:
"CastSpell – {hero name} – {MP needed} – {spell name}"
	•	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
	•	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
	•	If the hero is unable to cast the spell print:
	•	"{hero name} does not have enough MP to cast {spell name}!"
"TakeDamage – {hero name} – {damage} – {attacker}"
	•	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
	•	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
	•	If the hero has died, remove him from your party and print:
	•	"{hero name} has been killed by {attacker}!"
"Recharge – {hero name} – {amount}"
	•	The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to
    200. (the MP can't go over the maximum value).
	•	 Print the following message:
	•	"{hero name} recharged for {amount recovered} MP!"
"Heal – {hero name} – {amount}"
	•	The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value
	(100), HP is increased to 100 (the HP can't go over the maximum value).
	•	 Print the following message:
	•	"{hero name} healed for {amount recovered} HP!"


Input
	•	On the first line of the standard input, you will receive an integer n
	•	On the following n lines, the heroes themselves will follow with their hit points and mana points
	separated by a space in the following format
	•	You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given


Output
	•	Print all members of your party who are still alive, in the following format (their HP/MP need to be indented 2 spaces):
"{hero name}
  HP: {current HP}
  MP: {current MP}"""


number_of_heroes = int(input())
hero_dict = {}


for _ in range(number_of_heroes):
    hero_info = input()
    hero_name, *info = hero_info.split(" ")
    hp, mana = info
    hp = int(hp)
    mana = int(mana)
    if hp >= 100:
        hp = 100
    if mana >= 200:
        mana = 200
    hero_dict[hero_name] = {'hp': hp, 'mana': mana}

command_line = input()
while not command_line == 'End':
    command, hero_name, *info = command_line.split(" - ")
    if command == 'CastSpell':
        mp_needed, spell_name = info
        if hero_dict[hero_name]['mana'] >= int(mp_needed):
            hero_dict[hero_name]['mana'] -= int(mp_needed)
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero_dict[hero_name]['mana']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command == 'TakeDamage':
        damage, atacker = info
        hero_dict[hero_name]['hp'] -= int(damage)
        if hero_dict[hero_name]['hp'] <= 0:
            print(f"{hero_name} has been killed by {atacker}!")
            hero_dict.pop(hero_name)
        else:
            print(f"{hero_name} was hit for {damage} HP by {atacker} and now has {hero_dict[hero_name]['hp']} HP left!")
    elif command == 'Recharge':
        amount = info[0]
        if hero_dict[hero_name]['mana'] + int(amount) >= 200:
            amount = 200 - hero_dict[hero_name]['mana']
            hero_dict[hero_name]['mana'] = 200
        else:
            hero_dict[hero_name]['mana'] += int(amount)
        print(f"{hero_name} recharged for {amount} MP!")
    elif command == 'Heal':
        amount = info[0]
        if hero_dict[hero_name]['hp'] + int(amount) >= 100:
            amount = 100 - hero_dict[hero_name]['hp']
            hero_dict[hero_name]['hp'] = 100
        else:
            hero_dict[hero_name]['hp'] += int(amount)
        print(f"{hero_name} healed for {amount} HP!")
    command_line = input()
for hero, info in hero_dict.items():
    print(f"{hero}\nHP: {info['hp']}\nMP: {info['mana']}")




