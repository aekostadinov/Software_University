"""First, you will receive a sequence of integers representing the number of materials for crafting toys in one box. 
After that, you will be given another sequence of integers – their magic level.Your task is to mix materials with
magic so you can craft presents, listed in the table below with the exact magic level:

Present	        Magic needed
Doll	        150
Wooden train	250
Teddy bear	    300
Bicycle 	    400

You should take the last box with materials and the first magic level value to craft a toy. Their multiplication 
calculates the total magic level. If the result equals one of the levels described in the table above, you craft
the present and remove both materials and magic value. Otherwise:
    -If the product of the operation is a negative number, you should sum the values together, remove them both 
from their positions, and add the result to the materials.
    -If the product doesn't equal one of the magic levels in the table and is a positive number, remove only the
magic value and increase the material value by 15.
    -If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.Stop 
crafting presents when you run out of boxes of materials or magic level values.Your task is considered done if
you manage to craft either one of the pairs:
    -a doll and a train
    -a teddy bear and a bicycle
    
Input
    -The first line of input will represent the values of boxes with materials - integers, separated by a single space
    -On the second line, you will be given the magic values - integers again, separated by a single space

Output
    -On the first line - print whether you've succeeded in crafting the presents:
        o"The presents are crafted! Merry Christmas!"
        o"No presents this Christmas!"
    -On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
        o"Materials left: {material_N}, {material_N-1}, … {material_1}"
        o"Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
    -On the next lines print the presents you have crafted, ordered alphabetically in the format:
        o"{toy_name1}: {amount} {toy_name2}: {amount}...{toy_nameN}: {amount}"""
from collections import deque

materials_for_crafting_toys = [int(num) for num in input().split()]  # last
magic_level = deque([int(num) for num in input().split()])  # first
type_of_presents = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
crafted_presents = {}
while materials_for_crafting_toys and magic_level:
    current_magic_level = magic_level[0]
    current_material = materials_for_crafting_toys[-1]
    current_multiplier = current_magic_level * current_material
    if current_multiplier in type_of_presents:
        present = type_of_presents[current_multiplier]
        if present not in crafted_presents:
            crafted_presents[present] = 0
        crafted_presents[present] += 1
        magic_level.popleft()
        materials_for_crafting_toys.pop()
    elif current_multiplier < 0:
        sum_of_values = current_magic_level + current_material
        magic_level.popleft()
        materials_for_crafting_toys.pop()
        materials_for_crafting_toys.append(sum_of_values)
    elif current_multiplier > 0 and current_multiplier not in type_of_presents:
        magic_level.popleft()
        materials_for_crafting_toys[-1] += 15
    if current_magic_level == 0:
        magic_level.popleft()
    if current_material == 0:
        materials_for_crafting_toys.pop()
if ('Bicycle' in crafted_presents and 'Teddy bear' in crafted_presents) or (
        'Doll' in crafted_presents and 'Wooden train' in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials_for_crafting_toys:
    materials_for_crafting_toys.reverse()
    print(f"Materials left: {', '.join(str(num) for num in materials_for_crafting_toys)}")
if magic_level:
    print(f"Magic left: {', '.join(str(num) for num in magic_level)}")
if crafted_presents:
    crafted_presents = sorted(crafted_presents.items())
    for item in crafted_presents:
        print(f"{item[0]}: {item[1]}")

