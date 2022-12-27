"""Create a function called even_odd() that can receive a different quantity of numbers and a command at the end.
The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list. Submit
only the function in the judge system.Submit only your function in the judge system."""

def even_odd(*args):
    numbers = [num for num in args if isinstance(num,int)]
    if 'even' in args:
        return [int(num) for num in numbers if num % 2 == 0]
    elif 'odd' in args:
        return [int(num) for num in numbers if num % 2 != 0]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))