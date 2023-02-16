"""Create a function called get_magic_triangle which will receive a single parameter (integer n) and it should create a
magic triangle which follows those rules:
    -We start with this simple triangle [[1], [1, 1]]
    -We generate the next rows until we reach n amount of rows
    -Each number in each row is equal to the sum of the two numbers right above it in the triangle
    -If the current number has no neighbor to the upper left/rigth, we just take the existing neighbor
After you create the magic triangle, return it as a multidimensional list. Here is an example with n = 5"""


def get_magic_triangle(n):
    matrix = [[1], [1, 1]]
    counter = 1
    for index in range(0, n-2):
        counter += 1
        current_matrix = [1,1]
        for index in range(1, counter):
            current_number = matrix[-1][index-1] + matrix[-1][index]
            current_matrix.insert(index, current_number)
        matrix.append(current_matrix)
    return matrix

# get_magic_triangle(5)
