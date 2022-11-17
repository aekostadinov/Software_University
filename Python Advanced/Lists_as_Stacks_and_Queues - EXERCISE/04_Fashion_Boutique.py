"""You own a fashion boutique and receive a delivery of a huge box of clothes, represented as a sequence
of integers. On the following line, you will be given an integer representing the capacity for one rack in your store.
You must arrange the clothes in the store and use the racks to hang up every piece of clothing. You start from the
 last piece of clothing on the top of the pile to the first one at the bottom. Use a stack for this purpose.
 Each piece of clothing has its value (an integer). You must sum their values while you take them out of the box:
· If the sum becomes equal to the capacity of the current rack, you must take a new one for the next clothes
(if there are any left in the box).
· If the sum becomes greater than the capacity, do not hang the piece of clothing on the current rack.
Take a new rack and then hang it up.In the end, print how many racks you have used to hang up the clothes.

Input

· On the first line, you will be given a sequence of integers representing the clothes in the box, separated by a
single space.

· On the second line, you will be given an integer representing the capacity of a rack.

Output

· Print the number of racks needed to hang up the clothes from the box."""


stack_of_clothes = [int(num) for num in input().split()]
capacity_of_one_rack = int(input())
current_sum = 0
number_of_racks = 1

while stack_of_clothes:
    current_cloth = stack_of_clothes.pop()
    current_sum += current_cloth
    if current_sum == capacity_of_one_rack:
        number_of_racks += 1
    elif current_sum > capacity_of_one_rack:
        number_of_racks += 1
        stack_of_clothes.append(current_cloth)
    current_sum = 0
print(number_of_racks)


