"""On the first line, you will be given a string containing all of your stops.
Until you receive the command "Travel", you will be given some commands to manipulate
that initial string. The commands can be:
	•	"Add Stop:{index}:{string}":
	•	Insert the given string at that index only if the index is valid
	•	"Remove Stop:{start_index}:{end_index}":
	•	Remove the elements of the string from the starting index to the end index (inclusive) if
	both indices are valid
	•	"Switch:{old_string}:{new_string}":
	•	If the old string is in the initial string, replace it with the new one (all occurrences)
Note: After each command, print the current state of the string if it is valid!
After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"

Input / Constraints
	•	JavaScript: you will receive a list of strings
	•	An index is valid if it is between the first and the last element index (inclusive)
	(0 ….. Nth) in the sequence.

Output
	•	Print the proper output messages in the proper cases as described in the problem description"""



console_str = input()

command_line = input()

while not command_line == 'Travel':
    command = command_line.split(":")
    if command[0] == 'Add Stop':
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(console_str):
            console_str = console_str[:index] + string + console_str[index:]
    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(console_str) and 0 <= end_index < len(console_str):
            console_str = console_str[:start_index] + console_str[end_index + 1:]
    elif command[0] == 'Switch':
        old_string = command[1]
        new_string = command[2]
        if old_string in console_str:
            console_str = console_str.replace(old_string, new_string)
    print(console_str)
    command_line = input()
print(f"Ready for world tour! Planned stops: {console_str}")