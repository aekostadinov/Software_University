"""Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated
by a comma and a space ", ". You should find the matrix's diagonals, prints them and their sum in the format:
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}"""

# size = int(input())
# matrix = [input().split(", ") for _ in range(size)]
# primary = []
# secondary = []
# for s in range(size):
#     p_num = int(matrix[s][s])
#     primary.append(p_num)
#     s_num = int(matrix[s][size - s - 1])
#     secondary.append(s_num)
# print(f"Primary diagonal: {', '.join(str(num) for num in primary)}. Sum: {sum(primary)}")
# print(f"Secondary diagonal: {', '.join(str(num) for num in secondary)}. Sum: {sum(secondary)}")


### Varian 2 ###
size = int(input())
matrix = [input().split(", ") for _ in range(size)]
primary = [matrix[s][s] for s in range(size)]
secondary = [matrix[s][size - s - 1] for s in range(size)]
print(f"Primary diagonal: {', '.join(str(num) for num in primary)}. Sum: {sum(int(x) for x in primary)}")
print(f"Secondary diagonal: {', '.join(str(num) for num in secondary)}. Sum: {sum(int(x) for x in secondary)}")

