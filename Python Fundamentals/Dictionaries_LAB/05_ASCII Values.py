"""Write a program that receives a list of characters separated by ", ".
It should create a dictionary with each character as a key and its ASCII
value as a value. Try solving that problem using comprehension."""




chars_input = input().split(", ")
chars_dict = {chars_input[index]:ord(chars_input[index]) for index in range(len(chars_input))}
print(chars_dict)

