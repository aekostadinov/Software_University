"""Write a program that receives a sequence of numbers (integers) separated by a single space. It should print
a list of only the even numbers. Use filter()"""


def is_even(digit):
    if digit % 2 == 0:
        return True
    else:
        return False


numbers = [int(digit) for digit in input().split()]
filtered_numbers = filter(is_even, numbers)
final_result = [number for number in filtered_numbers]
print(final_result)