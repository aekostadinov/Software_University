number_of_electrons = int(input())
output_list = []
max_value = 2
n = 1

while max_value <= number_of_electrons:
    output_list.append(max_value)
    number_of_electrons -= max_value
    n += 1
    max_value = 2 * n * n
if (max_value > number_of_electrons) and (number_of_electrons != 0):
    output_list.append(number_of_electrons)

print(output_list)



# distributed_el = []
# shell = 0
# num_e = int(input())
# while num_e > 1:
#     shell += 1
#     shell_nums = 2 * (shell**2)
#     if num_e < shell_nums:
#         shell_nums = num_e
#         num_e = 0
#     else:
#         num_e -= shell_nums
#     distributed_el.append(shell_nums)
# print(distributed_el)


