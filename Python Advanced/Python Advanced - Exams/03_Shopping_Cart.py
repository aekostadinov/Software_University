


def shopping_cart(*args):
    output = ''
    limit_profucts = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    result = {"Soup": [], "Pizza": [], "Dessert": []}
    for tup in args:
        if tup == "Stop":
            break
        else:
            meal, product = tup
            if product not in result[meal]:
                if len(result[meal]) < limit_profucts[meal]:
                    result[meal].append(product)
    for key in result.keys():
        result[key] = sorted(result[key])
    sorted_dict = dict(sorted(result.items(),key=lambda x:(-len(x[1]), x[0])))
    if not result["Soup"] and not result["Pizza"] and not result["Dessert"]:
        return "No products in the cart!"
    else:
        for meal, products in sorted_dict.items():
            output += f"{meal}:" + "\n"
            for el in products:
                output += f" - {el}" + "\n"
        return output





### VARIANT 2###

def shopping_cart(*args):
    cart = {'Pizza': [], 'Soup': [], 'Dessert': []}
    for tuple_ in args:
        meal = tuple_[0]
        product = tuple_[1]
        if tuple_ == 'Stop':
            break
        if meal == 'Pizza' and len(cart['Pizza']) == 4:
            continue
        elif meal == 'Soup' and len(cart['Soup']) == 3:
            continue
        elif meal == 'Dessert' and len(cart['Dessert']) == 2:
            continue
        if product not in cart[meal]:
            cart[meal].append(product)

    for value in cart.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    sorted_cart = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for tuple_ in sorted_cart:
        result += f"{tuple_[0]}:\n"
        sorted_product = sorted(tuple_[1])
        for product in sorted_product:
            result += f" - {product}\n"

    return result


# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))