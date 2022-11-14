n = int(input())
sum_of_chars = 0

for _ in range(n):
    command = input()
    sum_of_chars += ord(command)

print(f"The sum equals: {sum_of_chars}")

