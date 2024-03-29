"""You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries.
 Each query is one of these four types:

· '1 {number}' – push the number (integer) into the stack
· '2' – delete the number at the top of the stack
· '3' – print the maximum number in the stack
· '4' – print the minimum number in the stack

It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom in the following format:

"{n}, {n1}, {n2}, ... {nn}"""


stack = []

number_of_commands = int(input())
for _ in range(number_of_commands):
    console_command = [int(num) for num in input().split()]
    first_num = console_command[0]
    if first_num == 1:
        stack.append(console_command[1])
    if len(stack) > 0:
        if first_num == 2:
            stack.pop()
        elif first_num == 3:
            print(max(stack))
        elif first_num == 4:
            print(min(stack))
print(', '.join(str(stack.pop()) for _ in range(len(stack))))

### Variant 2 ###

# from collections import deque
#
# numbers = deque()
#
# map_functions = {
#     1: lambda x: numbers.append(x[1]),
#     2: lambda x: numbers.pop() if numbers else None,
#     3: lambda x: print(max(numbers)) if numbers else None,
#     4: lambda x: print(max(numbers)) if numbers else None,
# }
#
# for _ in range(int(input())):
#     numbers_data = [int(x) for x in input().split()]
#     map_functions[numbers_data[0]](numbers_data)
#
# numbers.reverse()
#
# print(*numbers, sep=", ")
