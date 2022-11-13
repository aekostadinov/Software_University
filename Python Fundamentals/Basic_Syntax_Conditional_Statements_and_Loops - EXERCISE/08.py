number_of_coffees = 0
command = input()

while not command == 'END':
    if command == 'coding':
        number_of_coffees += 1
    elif command == 'CODING':
        number_of_coffees += 2
    elif command == 'dog' or command == 'cat':
        number_of_coffees += 1
    elif command == 'DOG' or command == 'CAT':
        number_of_coffees += 2
    elif command == 'movie':
        number_of_coffees += 1
    elif command == 'MOVIE':
        number_of_coffees += 2
    command = input()
if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)


