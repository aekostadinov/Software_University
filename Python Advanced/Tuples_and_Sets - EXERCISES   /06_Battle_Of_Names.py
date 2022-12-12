"""You will receive a number N. On the following N lines, you will be receiving names. You should sum the ASCII values
of each letter in the name and integer divide it by the number of the current row (starting from 1). Save the result to
a set of either odd or even numbers, depending on if the resulting number is odd or even. After that, sum the values of
each set.
· If the sums of the two sets are equal, print the union of the values, separated by ", ".
· If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values,
separated by ", ".
· If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values,
separated by ", ".

NOTE: On every operation, the starting set should be the odd set"""

count_of_names = int(input())
even_set = set()
odd_set = set()
for row in range(1,count_of_names+1):
    name = input()
    current_ascii_sum = 0
    for ch in name:
        current_ascii_sum += ord(ch)
    current_ascii_sum = int(current_ascii_sum / row)
    if current_ascii_sum % 2 == 0:
         even_set.add(current_ascii_sum)
    else:
        odd_set.add(current_ascii_sum)
if sum(even_set) == sum(odd_set):
    result = even_set.union(odd_set)
elif sum(even_set) > sum(odd_set):
    result = even_set.symmetric_difference(odd_set)
else:
    result = odd_set.difference(even_set)
print(*result, sep=', ')

