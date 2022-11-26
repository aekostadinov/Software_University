"""On the first line, you will receive a string. On the second line, you will receive a second string. 
Write a program that removes all the occurrences of the first string in the second until there is no match. 
At the end, print the remaining string."""

def replace_all_occurrences(first_string, second_string):
    while first_string in second_string:
        second_string = second_string.replace(first_string,'')

    return second_string

print(replace_all_occurrences(input(),input()))