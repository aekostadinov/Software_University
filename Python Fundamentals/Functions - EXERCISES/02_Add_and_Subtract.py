"""You will receive three integer numbers.

Write functions named:
· sum_numbers() that returns the sum of the first two integers
· subtract() that returns the difference between the returned result of the first function and the third integer

Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
Print the result of the subtract() function on the console"""

def sum_numbers(first, second):
    result = first + second
    return result


def subtract(first_two, third):
    result = first_two - third
    return result


def add_and_subtract(first, second, third):
    sum_of_the_first_two = sum_numbers(first, second)
    result = subtract(sum_of_the_first_two, third)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))