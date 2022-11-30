"""On the first line, you will receive a number n. On the next n lines, you will be given some information about the
plants that you have discovered in the format: "{plant}<->{rarity}". Store that information because you will need it
later. If you receive a plant more than once, update its rarity.
After that, until you receive the command "Exhibition", you will be given some of these commands:
	•	"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
	•	"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
	•	"Reset: {plant}" – remove all the ratings of the given plant
Note: If any given plant name is invalid, print "error"

After the command "Exhibition", print the information that you have about the plants in the following format:
"Plants for the exhibition: - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
- {plant_name2}; Rarity: {rarity}; Rating: {average_rating} …
- {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
The average rating should be formatted to the second decimal place.

Input / Constraints
	•	You will receive the input as described above
	•	JavaScript: you will receive a list of strings

Output
	•	Print the information about all plants as described above"""

def rate_command(info):
    plant, rating = info.split(" - ")
    rating = int(rating)
    if plant in plant_info:
        plant_info[plant]['rating'].append(rating)


def update_command(info):
    plant, new_rarity = info.split(" - ")
    new_rarity = int(new_rarity)
    plant_info[plant]['rarity'] = new_rarity

def plant_validation(info):
    plant = info.split(" - ")
    if plant[0] not in plant_info:
        print('error')
        return False
    return True

number_of_plants = int(input())
plant_info = {}

for _ in range(number_of_plants):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    plant_info[plant] = plant_info.get(plant,{'rarity': rarity, 'rating':[]})

command_line = input()



while not command_line == 'Exhibition':
    command, *rest_info = [info for info in command_line.split(": ")]
    if not plant_validation(*rest_info):
        command_line = input()
        continue
    if command == 'Rate':
        rate_command(*rest_info)
    elif command == 'Update':
        update_command(*rest_info)
    elif command == 'Reset':
        plant = rest_info[0]
        plant_info[plant]['rating'].clear()
    command_line = input()

print("Plants for the exhibition:")
for plant, info in plant_info.items():
    if info['rating']:
        average_rating = sum(info['rating']) / len(info['rating'])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {info['rarity']}; Rating: {average_rating:.2f}")














