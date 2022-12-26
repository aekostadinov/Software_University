"""White a function called sorting_cheeses that receives keywords arguments:
    -The key represents the name of the cheese
    -The value is a list of quantities (integers) of the pieces of the given cheese
The function should return the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind
in descending order. If two or more cheeses have the same number of pieces, sort them by their names in ascending
order (alphabetically). For each kind of cheese, return their pieces quantities in descending order."""

def sorting_cheeses(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''
    for key, value in kwargs:
        result += key + '\n'
        value = sorted(value, reverse=True)
        result += ('\n'.join(str(el) for el in value)) + '\n'
    return result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    ))
