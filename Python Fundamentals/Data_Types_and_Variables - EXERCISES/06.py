# number_of_counts = int(input())
#
# for num in range(97, 97 + number_of_counts):
#     char_1 = chr(num)
#     for num in range(97, 97 + number_of_counts):
#         char_2 = chr(num)
#         for num in range(97, 97 + number_of_counts):
#             char_3 = chr(num)
#             print(f'{char_1}{char_2}{char_3}')


number_of_alphabetical = int(input())

for i in range(0,number_of_alphabetical):
    for j in range(0,number_of_alphabetical):
        for k in range(0,number_of_alphabetical):
            print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}')










