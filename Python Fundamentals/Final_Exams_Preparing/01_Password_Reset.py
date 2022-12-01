"""Write a password reset program that performs a series of commands upon a predefined string. First, you will 
receive a string, and afterward, until the command "Done" is given, you will be receiving strings with commands 
split by a single space. The commands will be the following:
	•	"TakeOdd"
	•	 Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
	•	"Cut {index} {length}"
	•	Gets the substring with the given length starting from the given index from the password and removes its first 
occurrence, then prints the password on the console.
	•	The given index and the length will always be valid.
	•	"Substitute {substring} {substitute}"
	•	If the raw password contains the given substring, replaces all of its occurrences with the substitute text given
and prints the result.
	•	If it doesn't, prints "Nothing to replace!".
	
Input
	•	You will be receiving strings until the "Done" command is given.
	
Output
	•	After the "Done" command is received, print:
	•	"Your password is: {password}""""



console_text = input()

command = input()

while not command == 'Done':
    command, *info = command.split(" ")

    if command == 'TakeOdd':
        new_raw_password = ''
        for index in range(1, len(console_text), 2):
            new_raw_password += console_text[index]
        console_text = new_raw_password
        print(console_text)
    elif command == 'Cut':
        index, lenght = info
        index = int(index)
        lenght = int(lenght)
        substring = console_text[index: index + lenght]
        console_text = console_text.replace(substring,'',1)
        print(console_text)
    elif command == 'Substitute':
        substring, substitute = info
        if substring in console_text:
            console_text = console_text.replace(substring, substitute)
            print(console_text)
        else:
           print("Nothing to replace!")
    command = input()
print(f"Your password is: {console_text}")



