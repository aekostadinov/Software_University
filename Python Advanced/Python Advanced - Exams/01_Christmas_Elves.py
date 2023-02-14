"""First, you will receive a sequence of integers representing each elf's energy. On the following line, you will be
given another sequence of integers, each representing a number of materials in a box.
Your task is to calculate the total elves' energy used for making toys and the total number of successfully made toys.
You are very clever and have immediately recognized the pros and cons of the work process - the first elf takes the last
box of materials and tries to create the toy:
    -Usually, the elf needs energy equal to the number of materials. If he has enough energy, he makes the toy. His
energy decreases by the used energy, and the toy goes straight to Santa's bag. Then, the elf eats a cookie reward which
increases his energy by 1, and goes to the end of the line, preparing for the upcoming boxes.
    -Every third time one of the elves takes a box, he tries his best to be creative, and he will need twice as much
energy as usual. If he has enough, he manages to create 2 toys. Then, his energy decreases; he eats a cookie reward and
goes to the end of the line, similar to the first bullet.
    -Every fifth time one of the elves takes a box, he is a little clumsy and somehow manages to break the toy when he
just made it (if he made it). The toy is thrown away, and the elf doesn't get a cookie reward. However, his energy is
already spent, and it needs to be added to the total elves' energy.
        oIf an elf creates 2 toys, but he is clumsy, he breaks them.
    -If an elf does not have enough energy, he leaves the box of materials to the next elf. Instead of making the toy,
the elf drinks a hot chocolate which doubles his energy, and goes to the end of the line, preparing for the upcoming boxes.
Note: North Pole's social policy is very tolerant of the elves. If the current elf's energy is less than 5 units, he
does NOT TAKE a box, but he takes a day off. Remove the elf from the collection.
Stop crafting toys when you are out of materials or elves.

Input
    -The first line of input will represent each elf's energy - integers, separated by a single space
    -On the second line, you will be given the number of materials in each box - integers, separated by a single space
Output
    -On the first line, print the number of created toys: "Toys: {total_number_of_toys}"
    -On the second line, print the total used energy: "Energy: {total_used_energy}"
    -On the next two lines print the elves and boxes that are left, if there are any, otherwise skip the line:
        o"Elves left: {elf1}, {elf2}, … {elfN}"
        o"Boxes left: {box1}, {box2}, … {boxN}"""

from collections import deque

santa_bag = 0
total_energy = 0
elfs_energy = deque(int(num) for num in input().split()) # first
number_of_materials = deque(int(el) for el in input().split()) # last
counter = 1


while elfs_energy and number_of_materials:
    current_elf = elfs_energy[0]
    if current_elf < 5:
        elfs_energy.popleft()
        continue
    if counter % 3 == 0:
        current_material = 2 * number_of_materials[-1]
    else:
        current_material = number_of_materials[-1]
    if current_elf >= current_material:
        if counter % 3 == 0:
            santa_bag += 2
            if counter % 5 == 0:
                santa_bag -= 2
                current_elf -= 1
        else:
            santa_bag += 1
            if counter % 5 == 0:
                santa_bag -= 1
                current_elf -= 1
        current_elf -= current_material - 1
        elfs_energy.popleft()
        elfs_energy.append(current_elf)
        number_of_materials.pop()
        total_energy += current_material
    else:
        current_elf *= 2
        elfs_energy.popleft()
        elfs_energy.append(current_elf)
    counter += 1

print(f"Toys: {santa_bag}")
print(f"Energy: {total_energy}")
if elfs_energy:
    print(f"Elves left: {', '.join(str(el) for el in elfs_energy)}")
if number_of_materials:
    print(f"Boxes left: {', '.join(str(el) for el in number_of_materials)}")



