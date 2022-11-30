"""On the first line of the standard input, you will receive an integer n – the number of pieces you will initially
have. On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the
following format: "{piece}|{composer}|{key}".Then, you will be receiving different commands, each on a new line,
 separated by "|", until the "Stop" command is given:
	•	"Add|{piece}|{composer}|{key}":
	      •	You need to add the given piece with the information about it to the other pieces and print:
          "{piece} by {composer} in {key} added to the collection!"
	      •	If the piece is already in the collection, print:
          "{piece} is already in the collection!"
	•	"Remove|{piece}":
	      •	If the piece is in the collection, remove it and print:
          "Successfully removed {piece}!"
	      •	Otherwise, print:
          "Invalid operation! {piece} does not exist in the collection."
	•	"ChangeKey|{piece}|{new key}":
	      •	If the piece is in the collection, change its key with the given one and print:
          "Changed the key of {piece} to {new key}!"
	      •	Otherwise, print:
          "Invalid operation! {piece} does not exist in the collection."
Upon receiving the "Stop" command, you need to print all pieces in your collection in the following
 format:"{Piece} -> Composer: {composer}, Key: {key}"

Input/Constraints
	•	You will receive a single integer at first – the initial number of pieces in the collection
	•	For each piece, you will receive a single line of text with information about it.
	•	Then you will receive multiple commands in the way described above until the command "Stop".

Output
	•	All the output messages with the appropriate formats are described in the problem description."""

def add_command(piece, composer, key):
    if piece in piece_info:
        print(f"{piece} is already in the collection!")
    else:
        piece_info[piece] = {'composer': composer, 'key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")


def remove_command(piece):
    if piece in piece_info:
        del piece_info[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key_command(piece, new_key):
    if piece in piece_info:
        piece_info[piece]['key'] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


number_of_pieces = int(input())
piece_info = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    piece_info[piece] = {'composer': composer, 'key': key}

command_line = input()
while not command_line == 'Stop':
    command, *info = [item for item in command_line.split("|")]
    if command == 'Add':
        add_command(*info)
    elif command == 'Remove':
        remove_command(*info)
    elif command == 'ChangeKey':
        change_key_command(*info)
    command_line = input()
for piece, info in piece_info.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")
