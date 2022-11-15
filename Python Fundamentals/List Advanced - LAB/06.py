# nums = list(map(int,input().split(", ")))
# output_list = [index for index in range(len(nums)) if nums[index] % 2 == 0]
# print(output_list)


nums = list(map(int,input().split(", ")))
found_index_or_no = list(map(lambda x: x if nums[x] % 2 == 0 else 'no', range(len(nums))))
even_indexes = list(filter(lambda a: a != 'no', found_index_or_no))
print(even_indexes)

