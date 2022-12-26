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
