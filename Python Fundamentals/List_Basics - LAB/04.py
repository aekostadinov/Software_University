number_of_string = int(input())
searched_word = input()
all_strings = []
filtered_strings = []

for _ in range(number_of_string):
    txt = input()
    all_strings.append(txt)
    if searched_word in txt:
        filtered_strings.append(txt)
print(all_strings)
print(filtered_strings)
