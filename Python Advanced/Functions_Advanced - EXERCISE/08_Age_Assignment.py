"""Create a function called age_assignment() that receives a different number of names and a different number
of key-value pairs. The key will be a single letter (the first letter of each name) and the value - a number
(age). Find its first letter in the key-value pairs for each name and assign the age to the person's name.
Then, sort the names in ascending order (alphabetically) and return the information for each person on a new
line in the format: "{name} is {age} years old."
Submit only the function in the judge system."""


def age_assignment(*args, **kwargs):
    output = {}
    result = ''
    for name in args:
        first_letter = name[0]
        if first_letter in kwargs:
            output[name] = kwargs[first_letter]
    sorted_output = dict(sorted(output.items(), key=lambda x: x[0]))
    for name, age in sorted_output.items():
        result += f"{name} is {age} years old." + "\n"
    return result
    

print(age_assignment("Peter", "George", G=26, P=19))
