"""Write a program that reads a string from the console and replaces any sequence of the same letters
with a single corresponding letter."""


console_input = input()
output = console_input[0]
for index in range(1, len(console_input)):
    if console_input[index-1] == console_input[index]:
        continue
    else:
        output += console_input[index]
print(output)
