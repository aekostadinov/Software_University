console_nums = [int(n) for n in input().split(", ")]

boundary = 10

while True:
    current_list = []
    for people in console_nums:
        if people <= boundary:
            current_list.append(people)
    print(f"Group of {boundary}'s: {current_list}")
    [[console_nums.remove(x) for x in console_nums if x == y] for y in current_list]

    boundary += 10
    if len(console_nums) == 0:
        break