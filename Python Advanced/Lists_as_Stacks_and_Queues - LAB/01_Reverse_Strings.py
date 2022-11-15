""" Write program that:

· Reads an input string

· Reverses it using a stack

· Prints the result back on the console """

text = list(input())
stack = []

for i in range(len(text)):
    stack.append(text.pop())
print("".join(stack))