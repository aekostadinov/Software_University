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

