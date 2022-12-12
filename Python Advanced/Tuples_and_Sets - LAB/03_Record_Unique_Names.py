"""Write a program, which will take a list of names and print only the unique names in the list.
The order in which we print the result does not matter."""


count = int(input())
set_of_names = {input() for _ in range(count)}
for name in set_of_names:
    print(name)


#count = input()
#set_of_names = set()
#for _ in range(count):
#    set_of_names.add(input())
#for name in set_of_names:
#    print(name)