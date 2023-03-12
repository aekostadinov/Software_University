def shop_from_grocery_list(budget, grocery_list, *args):
    budget = int(budget)
    for _tuple in args:
        current_product, current_price = _tuple[0], float(_tuple[1])
        if budget >= current_price and current_product in grocery_list:
            budget -= current_price
            while current_product in grocery_list:
                grocery_list.remove(current_product)
        if budget < current_price and current_product in grocery_list:
            break
    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))


"""You did not buy all the products. Missing products: chips, meat."""
