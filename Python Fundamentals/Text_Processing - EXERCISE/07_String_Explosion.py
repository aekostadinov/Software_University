"""Write a program that reads a string from the console that contains:

· Explosions marked with '>'
· Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
· Any other characters

Your task is to delete x characters, starting after the exploded character ('>').
If you find another explosion mark ('>') while deleting characters, you should add
the strength to your previous explosion. You should not delete the explosion character – '>'.
When all characters are processed, print the final string."""

str_inp = input()
strenght_lst = []
output_lst = []
additional_value = 0

for index in range(len(str_inp)):
    if str_inp[index] == '>':
        power_value = int(str_inp[index + 1])
        strenght_lst.append(power_value)
str_inp = str_inp.split(">")
first_word = str_inp.pop(0)
for i in range(len(str_inp)):
    if strenght_lst[i] <= len(str_inp[i]):
        current_word = str_inp[i][strenght_lst[i]::]
        output_lst.append(current_word)
    else:
        current_word = ""
        output_lst.append(current_word)
        additional_value = strenght_lst[i] - len(str_inp[i])
        if i < len(strenght_lst) - 1:
            strenght_lst[i + 1] += additional_value
output_lst.insert(0, first_word)
print('>'.join(output_lst))
