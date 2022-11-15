def result(list):
    if len(set(list)) == 1:
        if list[0] == '1':
            print("First player won")
        elif list[0] == '2':
            print("Second player won")
        else:
            print("Draw!")

first_line, second_line, third_line = input().split(),input().split(),input().split()
first_vertical = [first_line[0], second_line[0], third_line[0]]
result(first_vertical)

second_vertical = [first_line[1], second_line[1], third_line[1]]
result(second_vertical)

third_vertical = [first_line[2], second_line[2], third_line[2]]
result(third_vertical)

first_horizontal = first_line
result(first_horizontal)

second_horizontal = second_line
result(second_horizontal)

third_horizontal = third_line
result(third_horizontal)

first_diagonal = [first_line[0], second_line[1], third_line[2]]
result(first_diagonal)

second_diagonal = [first_line[2], second_line[1], third_line[0]]
result(second_diagonal)



