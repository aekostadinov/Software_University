"""Create a class called Cup. Upon initialization it should receive size (number) and quantity (a number representing
how much liquid is in it).
The class should have two methods:
    -fill(milliliters) which will increase the amount of liquid in the cup with the given milliliters (if there is space
in the cup, otherwise ignore).
    -status() which will return the amount of free space left in the cup.
Submit only the class in the judge system. Do not forget to test your code."""


class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        free_space = self.size - self.quantity
        if free_space >= milliliters:
            self.quantity += milliliters

    def status(self):
        free_spae = self.size - self.quantity
        return free_spae


# cup = Cup(100, 50)
# print(cup.status())
# cup.fill(40)
# cup.fill(20)
# print(cup.status())