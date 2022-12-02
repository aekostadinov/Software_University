"""Write a function that receives two integer numbers. Calculate the factorial of each number.
Divide the first result by the second and print the division formatted to the second decimal point"""

def factorial_numbers(first, second):
    result_first_number, result_second_number = 1, 1
    for first_digit in range(1, first + 1):
        result_first_number *= first_digit
    for second_digit in range(1, second + 1):
        result_second_number *= second_digit
    return result_first_number / result_second_number


first_number = int(input())
second_number = int(input())
result = factorial_numbers(first_number, second_number)
print(f"{result:.2f}")