"""Write a program that reads a string with N integers from the console, separated by a single space,
 and reverses them using a stack. Print the reversed integers on one line, separated by a single space."""

list_of_nums = [int(num) for num in input().split()]
stack = []

while len(list_of_nums) > 0:
    stack.append(list_of_nums.pop())
print(" ".join(str(n) for n in stack))

### Variant 2 ###

# print(*input().split()[::-1], sep=" ")
