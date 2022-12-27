"""Write a concatenate() function that receives some strings as arguments and some named arguments (the key will be
a string, and the value will be another string).First, you should concatenate all arguments successively. Next, take
each key successively, and if it is present in the resulted string, change all matching parts with the key's value.
In the end, return the final string.See the examples for more clarification.
Submit only your function in the judge system."""

def concatenate(*args,**kwargs):
    result = ''
    for el in args:
        result += el
    for key,value in kwargs.items():
        if key in result:
            result = result.replace(key, kwargs[key])
    return result

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))