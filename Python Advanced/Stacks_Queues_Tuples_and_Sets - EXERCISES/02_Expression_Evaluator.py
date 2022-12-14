"""Write a program that evaluates a string expression. You will be given that string expression on the first line in
the form of numbers and operators separated with a single space from each other. Your job is to take that string
expression and calculate the result after evaluating it.To do that, you have to follow a simple rule. If, for example,
we have this string "2 4 * 1 3 -", the first time we meet an operator (*), we should take all the numbers we have so
far (2, 4), apply that operation to them, and save the result (8). The next time we meet an operator (-), we again take
all the numbers we have (8, 1, 3) and apply the operator to them in that order (8 - 1 - 3 = 4). In the end, we print the
result.All the numbers will always be integers, and the possible operators are  . It is important to keep the order of
the numbers (especially for "/" and "-" because the order matters). When having a division, you should round the result
to the lower integer.

Input
    -Single line: a string containing integers and operators

Output
    -Single number: the result after the evaluation"""

### Variant 1 ###
from collections import deque
from math import floor
sequence_elements = deque([int(num) if num[-1].isdigit() else num for num in input().split()])
possible_operators = ["*", "+", "-", "/"]
result = sequence_elements.popleft()
current_list_of_numbers = deque([])
while sequence_elements:
    current_item = sequence_elements.popleft()
    if current_item not in possible_operators:
        current_list_of_numbers.append(current_item)
    elif current_item in possible_operators:
        operator = current_item
        while current_list_of_numbers:
            current_num = current_list_of_numbers.popleft()
            result = floor(eval(f"{result} {operator} {current_num}"))
print(result)

### Variant 2 ###

from collections import deque
evaluation = deque([int(digit) if digit[-1].isdigit() else digit for digit in input().split()])
extracted_info = deque()
while evaluation:
    extracted_item = evaluation.popleft()
    if extracted_item in ['*', '/', '+', '-']:
        result = extracted_info.popleft()
        if extracted_item == '*':
            while extracted_info:
                result *= extracted_info.popleft()
        elif extracted_item == '+':
            while extracted_info:
                result += extracted_info.popleft()
        elif extracted_item == '-':
            while extracted_info:
                result -= extracted_info.popleft()
        elif extracted_item == '/':
            while extracted_info:
                result //= extracted_info.popleft()
        extracted_info = deque([result])
    else:
        extracted_info.append(extracted_item)
print(*extracted_info)
