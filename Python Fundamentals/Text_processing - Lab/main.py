

#1#








# print(''.join(map(lambda word: word * len(word), input().split(" "))))



# with object and classes

# class Example:
#     def __init__(self,words):
#         self.words = words
#
#     def repeat_func(self):
#         return ''.join(map(lambda x: x * len(x), self.words))
#
# words: list = input().split(" ")
# obj = Example(words)
# print(obj.repeat_func())


#3

# def replace_all_occurrences(first_string, second_string):
#     while first_string in second_string:
#         second_string = second_string.replace(first_string,'')
#
#     return second_string
#
# print(replace_all_occurrences(input(),input()))



#4

# banned_words = input().split(', ')
# text = input()
#
# for word in banned_words:
#     text = text.replace(word,'*'*len(word))
# print(text)


#5

# def get_digits(data):
#     return ''.join([str(ch) for ch in data if ch.isdigit()])
#
# def get_letters(data):
#     return ''.join([ch for ch in data if ch.isalpha()])
#
# def get_other_signs(data):
#     return ''.join([ch for ch in data if not ch.isdigit() and not ch.isalpha()])
#
#
# data = input()
# print(get_digits(data))
# print(get_letters(data))
# print(get_other_signs(data))

#1
# sequence_words = input().split(", ")
# is_valid = False
#
# for word in sequence_words:
#     if 3 <= len(word) <= 16:
#         for ch in word:
#             if ch.isalnum() or ch == '-'or ch == '_':
#                 is_valid = True
#             else:
#                 is_valid = False
#                 break
#         if is_valid:
#             print(word)

#2

# two_strings = list(sorted(input().split(), key=len))
# word_1, word_2 = two_strings
# total_sum = 0
# for index in range(len(word_1)):
#     current_sum = ord(word_1[index]) * ord(word_2[index])
#     total_sum += current_sum
# if len(word_2) > len(word_1):
#     for index in range(len(word_1), len(word_2)):
#         total_sum += ord(word_2[index])
# print(total_sum)

#3

# text = input().split('\\')
# for word in text:
#     if "." in word:
#         subtracted_list = word.split('.')
#         print(f"File name: {subtracted_list[0]}\nFile extension: {subtracted_list[1]}")


#4

# text = input()
# for ch in text:
#     encrypted_ch = chr(ord(ch) + 3)
#     print(encrypted_ch,end='')


#5

# console_inp = input()
#
# for index in range(len(console_inp)):
#     if console_inp[index] == ":":
#         print(f"{console_inp[index]}{console_inp[index + 1]}")

#6

# str_inp = input()
# str_output = str_inp[0]
#
# for index in range(len(str_inp) - 1):
#     if str_inp[index + 1] != str_inp[index]:
#         str_output += str_inp[index + 1]
# print(str_output)

#7
#
# str_inp = input()
# strenght_lst = []
# output_lst = []
# additional_value = 0
# for index in range(len(str_inp)):
#     if str_inp[index] == ">":
#         power_value = int(str_inp[index + 1])
#         strenght_lst.append(power_value)
# str_inp = str_inp.split(">")
# first_word = str_inp.pop(0)
# for i in range(len(str_inp)):
#     if strenght_lst[i] <= len(str_inp[i]):
#         current_word = str_inp[i][strenght_lst[i]::]
#         output_lst.append(current_word)
#     else:
#         current_word = ""
#         output_lst.append(current_word)
#         additional_value = strenght_lst[i] - len(str_inp[i])
#         if i < len(strenght_lst) - 1:
#             strenght_lst[i + 1] += additional_value
# output_lst.insert(0, first_word)
# print('>'.join(output_lst))


#7.2

# text = input()
# strength = 0
# new_text = ''
# for index in range(len(text)):
#     if strength > 0 and text[index] != ">":
#         strength -=1
#     elif text[index] == ">":
#         strength += int(text[index + 1])
#         new_text += text[index]
#     else:
#         new_text += text[index]
# print(new_text)


#9

# text = input().upper()
# unique_symbols = ''
# current_symbol = ''
# repetition = ''
# for index in range(len(text)):
#     if not text[index].isdigit():
#         current_symbol += text[index]
#     else:
#         for check_next_symbol in range(index, len(text)):
#             if not text[check_next_symbol].isdigit():
#                 break
#             repetition += text[check_next_symbol]
#         repetition = int(repetition)
#         unique_symbols += current_symbol * repetition
#         current_symbol = ''
#         repetition = ''
# print(f"Unique symbols used: {len(set(unique_symbols))}")
# print(unique_symbols)



#10





