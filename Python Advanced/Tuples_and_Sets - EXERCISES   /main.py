# 06_LAB


# ll = [1, 7, 6 , -1, 10, 8, -2, 12, 4, 7, 5, 2, 13 , 3, 9, 14, 11]
# target = 8
#
# targets = set()
# value_map = {}
# for value in ll:
#     if value in targets:
#         p1 = value
#         p2 = value_map[value]
#         print(f"{p1} + {p2} = {target}")
#     else:
#         targets.add(target-value)
#         value_map[target-value] = value





import time
start_time = time.time()
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for el in lst:
    print(el)
end_time = time.time()
print(end_time - start_time)

s_time = time.time()
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*lst,end='\n')
e_time = time.time()
print(e_time - s_time)

