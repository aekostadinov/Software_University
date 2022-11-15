"""You are given an algebraic expression with parentheses.
Scan through the string and extract each set of parentheses.

Print the result back on the console."""

# console_input = input()
# parentheses = []
#
# for i in range(len(console_input)):
#     if console_input[i] == '(':
#         parentheses.append(i)
#     elif console_input[i] == ')':
#         start_index = parentheses.pop()
#         print(console_input[start_index:i+1])

console_input = input()
parentheses = []

for index, symbol in enumerate(console_input):
    if symbol == '(':
        parentheses.append(index)
    elif symbol == ')':
        start_index = parentheses.pop()
        print(console_input[start_index:index+1])

