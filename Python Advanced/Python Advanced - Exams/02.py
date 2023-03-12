# def player_indexes(row,column):
#     for r in range(0, row):
#         for c in range(0,column):
#             if matrix[r][c] == "B":
#                 return r, c
#
# row, column = [int(num) for num in input().split()]
# matrix = [[char for char in input().split()] for _ in range(row)]
#
#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1)
# }
# moves_made = 0
# touched_oponents = 0
# my_position_r, my_position_c = player_indexes(row, column)
# command = input()
# while not command == 'Finish':
#     current_r, current_c = my_position_r + directions[command][0], my_position_c + directions[command][1]
#     if not (current_r in range(row) and current_c in range(column)):
#         command = input()
#         continue
#     elif matrix[current_r][current_c] == "O":
#         command = input()
#         continue
#     if matrix[current_r][current_c] == "-":
#         moves_made += 1
#         matrix[my_position_r][my_position_c] = "-"
#         matrix[current_r][current_c] = "B"
#     elif matrix[current_r][current_c] == "P":
#         moves_made += 1
#         touched_oponents += 1
#         matrix[my_position_r][my_position_c] = "-"
#         matrix[current_r][current_c] = "B"
#         if touched_oponents == 3:
#             break
#     my_position_r, my_position_c = current_r, current_c
#     command = input()
# print(f"Game over!\nTouched opponents: {touched_oponents} Moves made: {moves_made}")
#


print([x for x in "abc" if x == "a" else -1])