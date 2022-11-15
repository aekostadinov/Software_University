number_of_nums = int(input())
odd_nums = []
even_nums = []
negative_nums = []
positive_nums = []

for _ in range(number_of_nums):
    num = int(input())
    if num < 0:
        negative_nums.append(num)
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
    else:
        positive_nums.append(num)
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
command = input()
if command == 'even':
    print(even_nums)
elif command == 'odd':
    print(odd_nums)
elif command == 'positive':
    print(positive_nums)
elif command == 'negative':
    print(negative_nums)
