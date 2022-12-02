"""You will receive a single number. You should write a function that returns the sum of all even and all odd digits
 in a given number. The result should be returned as a single string in the format:

"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

Print the result of the function on the console."""


def odd_and_even(number):
    sum_of_even = [int(digit) for digit in number if int(digit) % 2 == 0]
    sum_of_odd = [int(digit) for digit in number if int(digit) % 2 != 0]
    return sum_of_even, sum_of_odd


number_as_string = input()
even_numbers_sum, odd_numbers_sum = odd_and_even(number_as_string)
print(f"Odd sum = {sum(odd_numbers_sum)}, Even sum = {sum(even_numbers_sum)}")