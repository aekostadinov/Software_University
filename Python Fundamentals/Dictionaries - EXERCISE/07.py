number_of_commands = int(input())
registered_information = {}

for _ in range(number_of_commands):
    command_line = input().split()
    command = command_line[0]
    if command == 'register':
        name = command_line[1]
        license_number = command_line[2]
        if name not in registered_information:
            print(f"{name} registered {license_number} successfully")
            registered_information[name] = license_number
        else:
            print(f"ERROR: already registered with plate number {license_number}")
    elif command == 'unregister':
        name = command_line[1]
        if name not in registered_information:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            registered_information.pop(name)
for key,value in registered_information.items():
    print(f"{key} => {value}")

