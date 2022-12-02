"""Write a program that receives a sequence of numbers (integers) separated by a single space. It should print
the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().

The output should be as follows:
· On the first line: "The minimum number is {minimum number}"
· On the second line: "The maximum number is {maximum number}"
· On the third line: "The sum number is: {sum of all numbers}"""

def min_max_and_sum(number):
    return min(number), max(number), sum(numbers)


numbers = [int(num) for num in input().split()]
min_of_numbers, max_of_numbers, sum_of_numbers = min_max_and_sum(numbers)
print(f"The minimum number is {min_of_numbers}")
print(f"The maximum number is {max_of_numbers}")
print(f"The sum number is: {sum_of_numbers}")