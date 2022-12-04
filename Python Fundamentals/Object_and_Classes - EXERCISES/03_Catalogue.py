"""Create a class Catalogue. The __init__ method should accept the name of the catalogue (string).
 Each catalogue should also have an attribute called products, an empty list. The class should also
  have three more methods:

· add_product(product_name: str) - adds the product to the products' list
· get_by_letter(first_letter: str) - returns a list containing only the products that start with the
given letter
· __repr__ - returns the catalogue info in the following format: "Items in the {name} catalogue:
 {item1} {item2}
…

{itemN}" The items should be sorted alphabetically in ascending order."""

class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [word for word in self.products if word[0] == first_letter]

    def __repr__(self):
        show_result = "Items in the {} catalogue:\n" \
                      "{}".format(self.name, '\n'.join(sorted(self.products)))
        return show_result