### 1 ###
number_a = int(input())
number_b = int(input())

print(f'Before:\na = {number_a}\nb = {number_b}')
a = number_b
b = number_a
print(f'After:\na = {a}\nb = {b}')


### 2 ###
num = int(input())
bul = True
for subtract in range(2,num):
    if num % subtract == 0:
        print('False')
        bul = False
        break
if bul and num > 1 :
    print('True')

### 3 ###
key = int(input())
number_of_lines = int(input())
output_message = ''

for _ in range(number_of_lines):
    char = input()
    output_message += chr(ord(char) + key)
print(output_message)

### 4 ###
n = int(input())
open_bracket = 0
closed_bracket = 0

for _ in range(n):
    console_command = input()
    if console_command == '(':
        open_bracket += 1
    elif console_command == ')':
        closed_bracket += 1
    if closed_bracket > open_bracket:
        print('UNBALANCED')
        exit()
    if abs(closed_bracket - open_bracket) > 1:
        print('UNBALANCED')
        exit()
if open_bracket == closed_bracket:
    print('BALANCED')
else:
    print('UNBALANCED')

