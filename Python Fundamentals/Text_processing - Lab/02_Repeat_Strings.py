"""Write a program that reads a sequence of strings, separated by a single space. Each string should be repeated 
N times, where N is the length of the string. Print the final strings concatenated into one string"""

seq = input().split()
final_lst = []
for str in seq:
    final_lst.append(str * len(str))
print("".join(final_lst))