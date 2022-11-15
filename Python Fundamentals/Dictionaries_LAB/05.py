chars_input = input().split(", ")
chars_dict = {chars_input[index]:ord(chars_input[index]) for index in range(len(chars_input))}
print(chars_dict)





















sequence = input().split(", ")
ascii_dictionary = {sequence[index]: ord(sequence[index]) for index in range(len(sequence))}
print(ascii_dictionary)