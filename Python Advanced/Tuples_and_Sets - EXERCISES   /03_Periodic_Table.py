"""Write a program that keeps all the unique chemical elements. On the first line, you will be given a number n -
the count of input lines that you will receive. On the following n lines, you will be receiving chemical compounds
separated by a single space. Your task is to print all the unique ones on separate lines (the order does not matter)"""

count_of_inputs = int(input())
sets_of_elements = set()
for _ in range(count_of_inputs):
    current_set = {element for element in input().split()}
    sets_of_elements = current_set.union(sets_of_elements)
print(*sets_of_elements,end='\n')

