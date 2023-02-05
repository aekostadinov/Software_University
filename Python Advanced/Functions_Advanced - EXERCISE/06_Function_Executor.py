"""Create a function called func_executor() that can receive a different number of tuples, each of which will have
exactly 2 elements: the first will be a function, and the second will be a tuple of the arguments that need to be
passed to that function. You should execute each function and return its result in the format:
"{function name} - {function result}"
For more clarification, see the examples below.
Submit only your function in the judge system."""


# def func_executor(*args):
#     output = ''
#     for element in args:
#         output += f"{element[0].__name__} - {element[0](*element[1])}" + '\n'
#     return output
#
#
# def make_upper(*strings):
#     result = tuple(s.upper() for s in strings)
#     return result
#
# def make_lower(*strings):
#     result = tuple(s.lower() for s in strings)
#     return result
#
# print(func_executor(
#     (make_upper, ("Python", "softUni")),
#     (make_lower, ("PyThOn",)),
# ))

### Variant 2 ###

def func_executor(*data):
    return '\n'.join([f"{func.__name__} - {func(*args)}" for func, args in data])

def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))