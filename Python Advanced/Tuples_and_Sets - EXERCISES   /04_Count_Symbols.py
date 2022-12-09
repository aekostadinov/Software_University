"""Write a program that reads a text from the console and counts the occurrences of each character in it.
Print the results in alphabetical (lexicographical) order"""


text = input()
set_of_chars = set()
for ch in text:
    set_of_chars.add(ch)
set_of_chars = sorted(set_of_chars)
for ch in set_of_chars:
    count_of_current_char = text.count(ch)
    print(f'{ch}: {count_of_current_char} time/s')
