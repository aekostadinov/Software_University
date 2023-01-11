"""Create a class called Vehicle. Upon initialization it should receive max_speed (number, optional; 150 by default)
and mileage (number). Create an instance variable called gadgets – empty list by default."""

class Vehicle:
    def __init__(self, mileage, max_speed = 150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []