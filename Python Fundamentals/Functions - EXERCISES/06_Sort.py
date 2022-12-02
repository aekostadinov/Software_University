"""Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a
sorted list of numbers in ascending order. Use sorted()"""


def sort_numbers(numbers):
    return sorted(numbers)


all_numbers = [int(number) for number in input().split()]
print(sort_numbers(all_numbers))