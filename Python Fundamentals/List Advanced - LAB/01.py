console_string = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
output_list = [element for element in console_string if element not in vowels]
print(''.join(output_list))

