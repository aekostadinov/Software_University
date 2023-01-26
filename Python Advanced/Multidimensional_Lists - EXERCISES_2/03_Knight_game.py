"""Chess is the oldest game, but it is still popular these days. It will be used only one chess piece for
this task - the Knight.A chess knight has 8 possible moves it can make, as illustrated. It can move to the
nearest square but not on the same row, column, or diagonal. (e.g., it can move two squares horizontally,
then one square vertically, or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.)
The knight game is played on a board with dimensions N x N.You will receive a board with "K" for knights and "0" for
empty cells. Your task is to remove knights until no knights that can attack one another with one move are left.
Always remove the knight who can attack the greatest number of knights. If there are two or more knights with
the same number of attacks, remove the top-left one.

Input
    -On the first line, you will receive integer N - the size of the board
    -On the following N lines, you will receive strings with "K" and "0"
Output
    -Print a single integer with the number of knights that need to be removed."""

# def attack_knights(row, column):
#     count_of_knights = 0
#     if (row - 2) in range(size) and (column - 1) in range(size):
#         if matrix[row - 2][column - 1] == 'K':
#             count_of_knights += 1
#     if (row - 2) in range(size) and (column + 1) in range(size):
#         if matrix[row - 2][column + 1] == 'K':
#             count_of_knights += 1
#     if (row - 1) in range(size) and (column - 2) in range(size):
#         if matrix[row - 1][column - 2] == 'K':
#             count_of_knights += 1
#     if (row - 1) in range(size) and (column + 2) in range(size):
#         if matrix[row - 1][column + 2] == 'K':
#             count_of_knights += 1
#     if (row + 2) in range(size) and (column - 1) in range(size):
#         if matrix[row + 2][column - 1] == 'K':
#             count_of_knights += 1
#     if (row + 2) in range(size) and (column + 1) in range(size):
#         if matrix[row + 2][column + 1] == 'K':
#             count_of_knights += 1
#     if (row + 1) in range(size) and (column - 2) in range(size):
#         if matrix[row + 1][column - 2] == 'K':
#             count_of_knights += 1
#     if (row + 1) in range(size) and (column + 2) in range(size):
#         if matrix[row + 1][column + 2] == 'K':
#             count_of_knights += 1
#     return count_of_knights
#
#
# def redifine_dict():
#     knights_dictionary = {}
#     for r in range(size):
#         for c in range(size):
#             if matrix[r][c] == 'K':
#                 count_of_knights = attack_knights(r, c)
#                 if count_of_knights > 0:
#                     knights_dictionary[(r, c)] = count_of_knights
#     knights_dictionary = dict(sorted(knights_dictionary.items(), key=lambda x: -x[1]))
#     return knights_dictionary
#
#
# size = int(input())
# matrix = [[char for char in input()] for _ in range(size)]
# counter = 0
# knights_dictionary = redifine_dict()
# while knights_dictionary:
#     counter += 1
#     for indexes, value in knights_dictionary.items():
#         row, column = indexes
#         knights_dictionary.pop(indexes)
#         matrix[row][column] = '0'
#         knights_dictionary = redifine_dict()
#         break
# print(counter)


### Variant 2 ###

size = int(input())
matrix = [list(input()) for _ in range(size)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1),
)

removed_knights = 0

while True:
    max_attacks = 0
    knights_with_most_attack_positions = []
    