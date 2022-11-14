key = int(input())
number_of_lines = int(input())
output_message = ''

for _ in range(number_of_lines):
    char = input()
    output_message += chr(ord(char) + key)
print(output_message)
