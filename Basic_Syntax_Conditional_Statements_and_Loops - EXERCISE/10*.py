first_string = input()
second_string = input()
left_side = ''
right_side = ''


for i in range(len(second_string)):
    if first_string[i] == second_string[i]:
        left_side += first_string[i]
        continue
    left_side += second_string[i]
    right_side = first_string[i+1::]
    print(left_side + right_side)
