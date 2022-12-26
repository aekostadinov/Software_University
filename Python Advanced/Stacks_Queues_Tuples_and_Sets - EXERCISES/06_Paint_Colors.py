"""Write a program that finds colors in a string. You will be given a string on a single line containing substrings
(separated by a single space) from which you will be able to form the following colors:
Main colors: "red", "yellow", "blue"
Secondary colors: "orange", "purple", "green"
To form a color, you should concatenate the first and the last substrings and check if you can get any of the above
colors' names. If there is only one substring left, you should use it to do the same check.You can only keep a secondary
color if the two main colors needed for its creation could be formed from the given substrings:
    -orange = red + yellow
    -purple = red + blue
    -green = yellow + blue
Note: You could find some of the main colors needed to keep a secondary color after it is found.
When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and
return them in the middle of the original string. If the string contains an odd number of substrings, you should put
the substrings one position ahead.For example, if you are given the string "re yellow bye" you could not form a color
with the substring "re" and "bye", so you should remove the last character and return them in the middle of the string:
"r by yellow".In the end, print out the list with colors in the order in which they are found.

Input
    -Single line string

Output
    -The list with the collected colors"""
from collections import deque

main_colors = ['red', 'yellow', 'blue']
sub_colors = ['orange', 'purple', 'green']

text = deque(input().split())

colors_que = deque()
while text:
    if len(text) > 1:
        first, second = text.popleft(), text.pop()
        straight, reverse = first + second, second + first
        if straight in main_colors or straight in sub_colors:
            colors_que.append(straight)
        elif reverse in main_colors or reverse in sub_colors:
            colors_que.append(reverse)
        else:
            edited_first, edited_second = first[:-1], second[:-1]
            middle = len(text) // 2
            if edited_first:
                text.insert(middle, edited_first)
            if edited_second:
                text.insert(middle, edited_second)
    else:
        substring = text.popleft()
        if substring in main_colors or substring in sub_colors:
            colors_que.append(substring)

for i in range(len(colors_que)):
    color = colors_que.popleft()
    if color == 'orange':
        if ('red' and 'yellow') in colors_que:
            colors_que.append(color)
    elif color == 'purple':
        if ('red' and 'blue') in colors_que:
            colors_que.append(color)
    elif color == 'green':
        if ('blue' and 'yellow') in colors_que:
            colors_que.append(color)
    else:
        colors_que.append(color)

print(list(colors_que))


