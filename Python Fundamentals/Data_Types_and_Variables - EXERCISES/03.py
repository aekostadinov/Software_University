from math import ceil

num_of_people = int(input())
capacity = int(input())

result = ceil(num_of_people / capacity)
print(result)
