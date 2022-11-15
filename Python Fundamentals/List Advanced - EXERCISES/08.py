words = input().split()

for word in words:
    lst_of_chars = []
    nums = ''
    for index in range(len(word)):
        if word[index].isdigit():
            nums += word[index]
        else:
            lst_of_chars.append(word[index])
    if len(lst_of_chars) >= 2:
        lst_of_chars[-1], lst_of_chars[0] = lst_of_chars[0], lst_of_chars[-1]
    result = chr(int(nums)) + ''.join(str(char) for char in lst_of_chars)
    print(result, end=' ')






