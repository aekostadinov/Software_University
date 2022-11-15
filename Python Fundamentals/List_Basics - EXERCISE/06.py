from sys import maxsize
lst_of_nums = list(map(int, input().split()))
count_of_nums = int(input())
minimum_num = maxsize
for index in range(count_of_nums):
    for i in range(len(lst_of_nums)):
        if lst_of_nums[i] < minimum_num:
            minimum_num = lst_of_nums[i]
    lst_of_nums.remove(minimum_num)
    minimum_num = maxsize
lst_of_nums = list(map(str,lst_of_nums))
print(', '.join(lst_of_nums))

