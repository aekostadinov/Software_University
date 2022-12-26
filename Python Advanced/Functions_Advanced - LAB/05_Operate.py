"""Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple
numbers (integers) as additional arguments (*args). The function should return the result of the operator applied
to all the numbers. For more clarification, see the examples below. Submit only your function in the Judge system.
Note: Be careful when you have multiplication and division"""


def operate(operator, *args):
    from math import prod
    from operator import sub, truediv
    from functools import reduce
    def addition():
        return sum(args)

    def subtract():
        return reduce(sub, args)

    def multiply():
        return prod(args)

    def divide():
        return reduce(truediv, args)

    if operator == "+":
        return addition()
    elif operator == '-':
        return subtract()
    elif operator == '*':
        return multiply()
    elif operator == '/':
        return divide()


print(operate("*", 1, 2, 5))
