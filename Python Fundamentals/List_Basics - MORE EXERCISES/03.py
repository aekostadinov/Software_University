sequence_numbers = input().split()
left_part = sequence_numbers[:int(len(sequence_numbers)/2)]
right_part = sequence_numbers[int(len(sequence_numbers)/2) + 1:]
sum_of_left_player = 0
sum_of_right_player = 0

for i in range(len(left_part)):
    if left_part[i] == "0":
        sum_of_left_player *= 0.8
    else:
        sum_of_left_player += float(left_part[i])
for j in range(len(right_part)-1,-1,-1):
    if right_part[j] == "0":
        sum_of_right_player *= 0.8
    else:
        sum_of_right_player += float(right_part[j])
if sum_of_left_player < sum_of_right_player:
    print(f"The winner is left with total time: {sum_of_left_player:.1f}")
else:
    print(f"The winner is right with total time: {sum_of_right_player:.1f}")
