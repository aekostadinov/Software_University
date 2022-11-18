"""You will be given a sequence consisting of parentheses.
 Your job is to determine whether the expression is balanced.
 A sequence of parentheses is balanced if every opening parenthesis
 has a corresponding closing parenthesis that occurs after the former.
  There will be no interval symbols between the parentheses.
  You will be given three types of parentheses: (), {}, and [].

{[()]} - Parentheses are balanced.
(){}[] - Parentheses are balanced.
{[(])} - Parentheses are NOT balanced.

Input
· On a single line, you will receive a sequence of parentheses.

Output
· For each test case, print on a new line "YES" if the parentheses are balanced.
· Otherwise, print "NO"""

parentheses = input()

opening_brackets = []
pairs = {'(':')', '[':']', '{':'}'}
balanced = True

for ch in parentheses:
    if ch in '([{':
        opening_brackets.append(ch)
    elif not opening_brackets:
        balanced = False
    else:
        last_opening_bracket = opening_brackets.pop()
        if pairs[last_opening_bracket] != ch:
            balanced = False
    if not balanced:
        break
if not balanced or opening_brackets:
    print('NO')
else:
    print('YES')









































# arithmetic_operation = input()
# check_opening_parenthesis = []
# for end_index, symbol in enumerate(arithmetic_operation):
#     if symbol == "(":
#         check_opening_parenthesis.append(end_index)
#     elif symbol == ")":
#         start_index = check_opening_parenthesis.pop()
#         print(arithmetic_operation[start_index:end_index + 1])