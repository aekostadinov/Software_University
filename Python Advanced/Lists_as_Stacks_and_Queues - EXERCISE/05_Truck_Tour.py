"""There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1)
(both inclusive). For each petrol pump, you will receive two pieces of information
(separated by a single space):
- The amount of petrol the petrol pump will give you
- The distance from that petrol pump to the next petrol pump (kilometers)
You are a truck driver, and you want to go all around the circle. You know that the truck
consumes 1 liter of petrol per 1 kilometer, and its tank has infinite petrol capacity.
In the beginning, the tank is empty, but you start your journey at a petrol pump so you can
fill it with the given amount of petrol.

Your task is to calculate the first petrol pump from where the truck will be able to complete
 the circle. You never miss filling its tank at a petrol pump.

Input
· On the first line, you will receive the number of petrol pumps - N
· On the next N lines, you will receive the amount of petrol that each petrol pump
will give and the distance between that petrol pump and the next petrol pump,
separated by a single space

Output
· An integer which will be the smallest index of a petrol pump from which you can start the tour"""


from collections import deque
queue = deque()

number_of_pumps = int(input())
current_index = 0
current_tank = 0

for _ in range(number_of_pumps):
    queue.append([int(n) for n in input().split()])

for _ in range(number_of_pumps):
    bul = True
    for _ in range(len(queue)):
        info = queue.popleft()
        queue.append(info)
        amount = int(info[0])
        distance = int(info[1])
        current_tank += amount - distance
        if current_tank < 0:
            bul = False
    if bul:
        break
    else:
        current_index += 1
        current_tank = 0
        queue.append(queue.popleft())
print(current_index)






# from collections import deque
#
# pumps_count = int(input())
# pumps = deque()
# for _ in range(pumps_count):
#     pumps.append([int(x) for x in input().split()])
#
# for attempt in range(pumps_count):
#     trunk = 0
#     failed = False
#     for petrol, distance in pumps:
#         trunk = trunk + petrol - distance
#         if trunk < 0:
#             failed = True
#             break
#     if failed:
#         pumps.append(pumps.popleft())
#     else:
#         print(attempt)
#         break