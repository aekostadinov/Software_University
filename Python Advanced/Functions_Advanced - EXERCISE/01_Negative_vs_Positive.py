"""You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers
from the positive. Find the total sum of the negatives and positives, and print the following:
    -On the first line, print the sum of the negatives
    -On the second line, print the sum of the positives
    -On the third line:
        oIf the absolute negative number is larger than the positive number:
"The negatives are stronger than the positives"
        oIf the positive number is larger than the absolute negative number:
"The positives are stronger than the negatives"

Note: you will not receive any zeroes in the input."""
def negative_positive(args):
    positive_sum = 0
    negative_sum = 0
    for el in args:
        if el < 0:
            negative_sum += el
        else:
            positive_sum += el
    if abs(negative_sum) > positive_sum:
        return f"{negative_sum}" + '\n' + f"{positive_sum}" + '\n' + "The negatives are stronger than the positives"
    else:
        return f"{negative_sum}" + '\n' + f"{positive_sum}" + '\n' + "The positives are stronger than the negatives"
sequence_nums = [int(num) for num in input().split()]
print(negative_positive(sequence_nums))
