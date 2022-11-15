to_do_list = [0] * 10

while True:
    command_line = input()
    if command_line == 'End':
        break
    command = command_line.split("-")
    priority = int(command[0]) - 1
    note = command[1]
    to_do_list.pop(priority)
    to_do_list.insert(priority, note)
result = [element for element in to_do_list if element != 0]
print(result)