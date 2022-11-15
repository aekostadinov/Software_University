lst_of_nums = input().split(", ")
lst_output = []

for i in range(len(lst_of_nums)):
    if not int(lst_of_nums[i]) == 0:
        lst_output.append(lst_of_nums[i])
for j in range(len(lst_of_nums)):
    if int(lst_of_nums[j]) == 0:
        lst_output.append(lst_of_nums[j])
lst_output = list(map(int, lst_output))
print(lst_output)




# numbers = input().split(", ")
# numbers = [int(item) for item in numbers]
# counter = 0
# while 0 in numbers:
#     numbers.remove(0)
#     counter += 1
# while counter >= 1:
#     numbers.append(0)
#     counter -= 1
# print(numbers)