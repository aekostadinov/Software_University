"""A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).

Write a function that receives an integer number and returns one of the following messages:

· "We have a perfect number!" - if the number is perfect.

· "It's not so perfect." - if the number is NOT perfect."""

def is_perfect(num):
    result = num // 2
    while result > 2:
        result //= 2
    if result == 1:
        return f"We have a perfect number!"
    elif result != 1:
        return f"It's not so perfect."


number = int(input())
result = is_perfect(number)
print(result)