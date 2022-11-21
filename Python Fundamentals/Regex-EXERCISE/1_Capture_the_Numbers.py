import re
valid_nums = []

pattern = r"\d+"
while True:
    text = input()
    if text == '':
        break
    matched_num = re.findall(pattern, text)
    valid_nums.extend(matched_num)

print(*valid_nums)



