"""Write a program that keeps track of people getting water from a dispenser
and the amount of water left at the end.

On the first line, you will receive the starting quantity of water (integer) in a dispenser.
Then, on the following lines, you will be given the names of some people who want to get water (each on a separate line) until you receive the command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":

- "{liters}" - litters (integer) that the current person in the queue wants to get.
Check if there is enough water in the dispenser for that person.

o If there is enough water, print "{person_name} got water" and remove him/her from the queue.

o Otherwise, print "{person_name} must wait" and remove the person from the queue without
 reducing the water in the dispenser.

- "refill {liters}" - add the given litters in the dispenser.

In the end, print how many liters of water have left in the format: "{left_liters} liters left"."""



from collections import deque
queue = deque([])

liters_in_dispenser = int(input())
command = input()

while not command == 'Start':
    queue.append(command)
    command = input()

command_line = input()
while not command_line == 'End':
    if command_line.isdigit():
        current_name = queue.popleft()
        if int(command_line) <= liters_in_dispenser:
            liters_in_dispenser -= int(command_line)
            print(f"{current_name} got water")
        else:
            print(f"{current_name} must wait")
    elif 'refill' in command_line:
        refill = command_line.split()
        refill_liters = int(refill[1])
        liters_in_dispenser += refill_liters
    command_line = input()
print(f"{liters_in_dispenser} liters left")

