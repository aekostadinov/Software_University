"""Create a class called PizzaDelivery. Upon initialization, it should receive a name (string), a price (float), and
ingredients (dictionary). The class should also have an instance attribute ordered set to False by default. You should
also create 3 additional instance methods:
    -add_extra(ingredient: str, quantity: int, price_per_quantity: float):
        oIf we already have this ingredient in our pizza, increase the ingredient quantity with the given one and update
the pizza price by adding the ingredient price for the given quantity
        oIf we do not have this ingredient in our pizza, we should add it and update the pizza price
    -remove_ingredient(ingredient: str, quantity: int, price_per_quantity: float):
        oIf we do not have this ingredient in our pizza, we should return the following message "Wrong ingredient
selected! We do not use {ingredient} in {pizza_name}!"
        oIf we have the ingredient, but we try to remove more than we have available, we should return the following
message "Please check again the desired quantity of {ingredient}!"
        oOtherwise, remove the given quantity of the ingredient and update the pizza price by removing the ingredient
price for the given quantity

    -make_order()
        oSet the attribute ordered to True and return the following message "You've ordered pizza {pizza_name} prepared
with {ingredient: quantity} and the price will be {price}lv.". The ingredients should be separated by a comma
and a space ", "
        oKeep in mind that once the pizza is ordered, no further changes are allowed. We should return the following
message if the customer tries to change it: "Pizza {name} already prepared, and we can't make any changes!"""


class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        self.price += price_per_quantity * quantity



    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if ingredient in self.ingredients and quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity



    def make_order(self):
        self.ordered = True
        result_products = [f"{product}: {str(quantity)}" for product, quantity in self.ingredients.items()]
        return f"You've ordered pizza {self.name} prepared with {', '.join(result_products)} and the price will" \
               f" be {int(self.price)}lv."

