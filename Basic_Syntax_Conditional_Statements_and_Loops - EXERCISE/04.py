divisor = int(input())
boundary = int(input())
largest_integer = 1

for num in range(boundary, divisor, -1):
    if (num % divisor == 0) and num > 0:
        largest_integer = num
        break
print(largest_integer)

