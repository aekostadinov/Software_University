command = input()
bul = True

while not command == 'Welcome!':
    name = command
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6 and not name == 'Voldemort':
        print(f"{name} goes to Hufflepuff.")
    elif name == 'Voldemort':
        print("You must not speak of that name!")
        bul = False
        break
    command = input()
if bul:
    print("Welcome to Hogwarts.")





