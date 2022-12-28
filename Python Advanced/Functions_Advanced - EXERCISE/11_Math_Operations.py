"""Write a function named math_operations that receives a different number of floats as arguments and 4 keyword
arguments. The keys will be single letters: "a", "s", "d", "m", and the values will be numbers.You need to take
each float argument from the sequence and do mathematical operations as follows:
    -The first element should be added to the value of the key "a"
    -The second element should be subtracted from the value of the key "s"
    -The third element should be divisor to the value of the key "d"
    -The fourth element should be multiplied by the value of the key "m"
    -Each result should replace the value of the corresponding key
    -You must repeat the same steps consecutively until you run out of numbers
Beware: You cannot divide by 0. If the operation could throw an error, you should skip the operation and continue to
the next one.After you finish calculating all numbers, sort the four elements by their values in descending order.
If two or more values are equal, sort them by their keys in ascending order (alphabetically).In the end, return each
key-value pair in the format "{key}: {value}" on separate lines. Each value should be formatted to the first decimal
point.For more clarifications, see the examples below.
Note: Submit only the function in the judge system

Input
    -There will be no input. Just parameters passed to your function.
    -All of the given numbers will be valid integers in the range [-100, 100]
Output
The function should return the final dictionary"""



def math_operations(*args, **kwargs):
    result = ''
    lst_of_floats = args
    symbols_dict = kwargs
    symbols = ["a", "s", "d", "m"]
    current_index = 0
    for num in lst_of_floats:
        if current_index >= len(symbols):
            current_index = 0
        if symbols[current_index] == "a":
            symbols_dict["a"] += num
        elif symbols[current_index] == "s":
            symbols_dict["s"] -= num
        elif symbols[current_index] == "d":
            if num != 0:
                symbols_dict["d"] /= num
        elif symbols[current_index] == "m":
            symbols_dict["m"] *= num
        current_index += 1
    sorted_result = dict(sorted(symbols_dict.items(),key=lambda x:(-x[1],x[0])))
    for key,value in sorted_result.items():
        result += f"{key}: {value:.1f}"+ "\n"
    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))