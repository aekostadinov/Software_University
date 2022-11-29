"""On the first line of the input, you will receive the encrypted message. After that, until the "Decode" command 
is given, you will be receiving strings with instructions for different operations that need to be
performed upon the concealed message to interpret it and reveal its true content. 
There are several types of instructions, split by '|'
    "Move {number of letters}":
      o  Moves the first n letters to the back of the string
    "Insert {index} {value}":
      o  Inserts the given value before the given index in the string
    "ChangeAll {substring} {replacement}":
      o  Changes all occurrences of the given substring with the replacement text
Input / Constraints
   On the first line, you will receive a string with a message.
   On the following lines, you will be receiving commands, split by '|' .
   
Output
   After the "Decode" command is received, print this message:
   "The decrypted message is: {message}""""

encrypted_message = input()

command_line = input()

while not command_line == 'Decode':
    command,*info = command_line.split("|")
    if command == 'Move':
        number_of_letters = int(info[0])
        current_message = encrypted_message[:number_of_letters]
        encrypted_message = encrypted_message[number_of_letters:] + current_message
    elif command == 'Insert':
        index = int(info[0])
        value = info[1]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command == 'ChangeAll':
        substring, replacement = info
        encrypted_message = encrypted_message.replace(substring,replacement)
    command_line = input()

print(f"The decrypted message is: {encrypted_message}")