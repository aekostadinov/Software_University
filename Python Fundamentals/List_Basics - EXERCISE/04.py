console_nums = input().split(', ')
number_of_beggars = int(input())
count = number_of_beggars
output_str = []
sum_for_each_beggar = 0
while count > 0:
    for index in range(count):
        for i in range(index, len(console_nums), number_of_beggars):
            sum_for_each_beggar += int(console_nums[i])
        output_str.append(sum_for_each_beggar)
        sum_for_each_beggar = 0
        count -= 1
        if count == 0:
            break
print(output_str)
