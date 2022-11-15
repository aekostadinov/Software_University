sequence_of_strings = input()
digits_lst = []
non_numbers_lst = []
take_lst = []
skip_lst = []
result = ''


for char in sequence_of_strings:
    if char.isdigit():
        digits_lst.append(char)
    else:
        non_numbers_lst.append(char)
non_numbers_string = ''.join(non_numbers_lst)
for index, element in enumerate(digits_lst):
    if index % 2 == 0:
        take_lst.append(element)
    else:
        skip_lst.append(element)
for index in range(len(take_lst)):
    taken_string_index = int(take_lst[index])
    skipped_string_index = int(skip_lst[index]) + int(take_lst[index])
    result += non_numbers_string[:taken_string_index]
    non_numbers_string = non_numbers_string[skipped_string_index:]
print(result)
