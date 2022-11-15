count = int(input())
wagons = [0] * count
console_input = input()

while not console_input == 'End':
    command = console_input.split(" ")
    if command[0] == 'add':
        people_add = int(command[1])
        wagons[-1] += people_add
    elif command[0] == 'insert':
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people
    elif command[0] == 'leave':
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people
    console_input = input()
print(wagons)

