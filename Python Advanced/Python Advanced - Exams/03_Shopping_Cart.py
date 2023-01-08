"""Write a function called shopping_cart that adds products to a shopping cart for the following three types of meals:
"Soup", "Pizza", and "Dessert". Every meal has a limit of products that can be added to it:
    -Soup: 3
    -Pizza: 4
    -Dessert: 2
Once you reach the limit of a meal, you should stop adding products to that meal.
The function will receive a different number of arguments. The arguments will be passed as tuples with two elements -
the first one is the type of meal, and the second is the product for the meal. You need to take each argument and make
a dictionary with the meal's name as a key and the products as a value of the corresponding key.
There are some additional requirements:
    -If you receive the same product for the same meal more than once, you must not add it again.
    -If you run into the word "Stop" (not tuple) as an argument, you must immediately stop adding products to the
cart - just sort and return the desired result as described below.
In the end, sort the meals by the number of bought products in descending order. If there are meals with an equal number
of products, sort them (the meals) by their name in ascending order (alphabetically). For each meal sort its products
in ascending order (alphabetically).
Return an output as described below.
Note: Submit only the function in the judge system

Input
    -There will be no input, just parameters passed to your function
Output
    -Return a string for each of the 3 types of a meal of the sorted result in the format:
        o"{meal_type}:"
        " - {first_product_added}"
        " - {second_product_added}"
        …
        " - {Nth_product_added}"
        oIf there are no products given for a meal, return just its name in the format shown above.
    -If there are NO products in the cart (at all), return the message: "No products in the cart!"""


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