"""Write a function called fill_the_box that receives a different number of arguments representing:
    -the height of a box
    -the length of a box
    -the width of a box
    -n-times a different number of cubes with exact size 1 x 1 x 1
    -a string "Finish"
Your task is to fill the box with the given cubes until the current argument equals "Finish".
Note: Submit only the function in the judge system

Input
    -There will be no input. Just parameters passed to your function.
Output
The function should return a string in the following format:
    -If, at the end, there is free space left in the box, print:
        o"There is free space in the box. You could put {free space in cubes} more cubes."
    -If there is no free space in the box, print:
        o"No more free space! You have {cubes left} more cubes."""





def fill_the_box(*args):
    height, lenght, width, *rest_info = args
    possible_number_cubes = height * lenght * width
    index_of_finish_command = rest_info.index("Finish")
    cubes = rest_info[:index_of_finish_command]
    number_of_cubes = sum(cubes)
    if possible_number_cubes > number_of_cubes:
        free_spaces = possible_number_cubes - number_of_cubes
        return f"There is free space in the box. You could put {free_spaces} more cubes."
    else:
        cubes_left = number_of_cubes - possible_number_cubes
        return f"No more free space! You have {cubes_left} more cubes."
