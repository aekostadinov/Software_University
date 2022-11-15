console_input = input().replace(" ", "")
chars_dict = {}

for char in console_input:
    if char not in chars_dict:
        chars_dict[char] = 0
    chars_dict[char] += 1
for char, count in chars_dict.items():
    print(f"{char} -> {count}")