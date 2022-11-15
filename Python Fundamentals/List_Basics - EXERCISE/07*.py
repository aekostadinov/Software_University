number_of_gifts = input().split()
console_input = input()
output_list = []

while not console_input == 'No Money':
    command = console_input.split(" ")
    if command[0] == "OutOfStock":
        if command[1] in number_of_gifts:
            for i in range(len(number_of_gifts)):
                if number_of_gifts[i] == command[1]:
                    number_of_gifts[i] = 'None'
    elif command[0] == 'Required':
        if 0 <= int(command[2]) < len(number_of_gifts):
            number_of_gifts[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        number_of_gifts[-1] = command[1]
    console_input = input()
for i in range(len(number_of_gifts)):
    if not number_of_gifts[i] == 'None':
        output_list.append(number_of_gifts[i])
print(' '.join(output_list))



