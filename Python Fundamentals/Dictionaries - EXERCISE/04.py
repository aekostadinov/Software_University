phone_book_dict = {}
command_line = input()
while not command_line.isdigit():
    command_line = command_line.split("-")
    name = command_line[0]
    phone_number = (command_line[1])
    phone_book_dict[name] = phone_number
    command_line = input()

count_of_names = int(command_line)
for _ in range(count_of_names):
    name = input()
    if name in phone_book_dict:
        print(f"{name} -> {phone_book_dict[name]}")
    else:
        print(f"Contact {name} does not exist.")

