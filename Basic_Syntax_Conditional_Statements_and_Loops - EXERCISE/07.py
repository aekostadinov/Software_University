command = input()
final_string = ''

while not command == 'End':
    if command != "SoftUni":
        for ch in command:
            final_string += ch * 2
        print(final_string)
    final_string = ''
    command = input()

