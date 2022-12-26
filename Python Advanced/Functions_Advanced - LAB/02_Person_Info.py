"""Write a function called get_info that receives a name, an age, and a town and returns a string in the format:
"This is {name} from {town} and he is {age} years old". Use dictionary unpacking when testing your function. Submit
only the function in the judge system."""

def get_info(**kwargs):
    return f"This is {kwargs.get('name')} from {kwargs.get('town')}" \
           f" and he is {kwargs.get('age')} years old"

print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))