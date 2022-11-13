lst = input().split(', ')
if lst[-1] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(lst)):
        if lst[i] == 'wolf':
            number_of_sheep = len(lst) - 1 - i
            print(f"Oi! Sheep number {number_of_sheep}! You are about to be eaten by a wolf!")
            break

# animals = input().split(", ")
# wolf_index = animals.index('wolf') + 1
# sheep_index = len(animals) - wolf_index
# if wolf_index == len(animals):
#     print("Please go away and stop eating my sheep")
# else:
#     print(f"Oi! Sheep number {sheep_index}! You are about to be eaten by a wolf!")