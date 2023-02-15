"""First, you will receive a sequence of integers representing the materials for every wedding present. After that,
you will be given another sequence of integers – Genie magic level for every aim to make a gift.
Your task is to mix materials with magic levels so you can make presents, listed in the table below.
Gift	            Magic needed
Gemstone	        100 to 199
Porcelain Sculpture	200 to 299
Gold	            300 to 399
Diamond Jewellery	400 to 499


To make a present, you should take the last integer of materials and sum it with the first magic level value. If the
result is between or equal to the numbers described in the table above, you make the corresponding gift and remove both
materials and magic value. Otherwise:
    -If the product of the operation is under 100:
        oAnd if it is an even number, double the materials, and triple the magic, then sum it again.
        oAnd if it is an odd number, double the sum of the materials and the magic level. Then, check again if it is
between or equal to any of the numbers in the table above.
    -If the product of the operation is more than 499, divide the sum of the material and the magic level by 2. Then,
check again if it is between or equal to any of the numbers in the table above.
    -If, however, the result is not between or equal to any of the numbers in the table above after performing the
calculation, remove both the materials and the magic level.
Stop crafting gifts when you are out of materials or magic level.
You have succeeded in crafting the presents when you've crafted either one of the pairs - a gemstone and a sculpture
or gold and jewellery.

Input
    -The first line of input will represent the values of materials - integers, separated by a single space
    -On the second line, you will be given the magic levels - integers, separated by a single space

Output
    -On the first line - print whether you have succeeded in crafting the presents:
        o"The wedding presents are made!"
    -On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
        o"Materials left: {material1}, {material2}, …"
        o"Magic left: {magicValue1}, {magicValue2}, …
    -On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
"{present1}: {amount}
{present2}: {amount}
…
{presentN}: {amount}"""


from collections import deque

def operations(current_sum):
        if 100 <= current_sum <= 199:
            gift_items["Gemstone"] += 1
        elif 200 <= current_sum <= 299:
            gift_items["Porcelain Sculpture"] += 1
        elif 300 <= current_sum <= 399:
            gift_items["Gold"] += 1
        elif 400 <= current_sum <= 499:
            gift_items["Diamond Jewellery"] += 1

values_of_materials = deque(int(num) for num in input().split())  # last
magic_levels = deque(int(num) for num in input().split())  # first
gift_items = {"Diamond Jewellery": 0, "Gemstone": 0, "Gold": 0, "Porcelain Sculpture": 0}
while values_of_materials and magic_levels:
    current_material = values_of_materials[-1]
    current_magic_level = magic_levels[0]
    current_sum = current_material + current_magic_level
    if 100 <= current_sum <= 499:
        values_of_materials.pop()
        magic_levels.popleft()
        operations(current_sum)
    else:
        if current_sum < 100 and current_sum % 2 == 0:
            current_material *= 2
            current_magic_level *= 3
            current_sum = current_material + current_magic_level
        elif current_sum < 100 and current_sum % 2 == 1:
            current_sum *= 2
        elif current_sum > 499:
            current_material /= 2
            current_magic_level /= 2
            current_sum = current_material + current_magic_level
        if 100 <= current_sum <= 499:
            operations(current_sum)
        values_of_materials.pop()
        magic_levels.popleft()
if (gift_items["Gemstone"] and gift_items["Porcelain Sculpture"]) or \
        (gift_items["Gold"] and gift_items["Diamond Jewellery"]):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if values_of_materials:
    print(f"Materials left: {', '.join(str(mat) for mat in values_of_materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(magic) for magic in magic_levels)}")
for key,value in gift_items.items():
    if value > 0:
        print(f"{key}: {value}")






