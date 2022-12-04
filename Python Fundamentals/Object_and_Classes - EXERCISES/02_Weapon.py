"""Create a class Weapon. The __init__ method should receive a number of bullets (integer).
Create an attribute called bullets to store that number. The class should also have the
 following methods:

· shoot()
o If there are bullets in the weapon, reduce them by 1 and return a message "shooting..."
o If there are no bullets left, return: "no bullets left"
· __repr__()
o Returns "Remaining bullets: {amount_of_bullets}" o You can read more about the method here: link"""

class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        message = ""
        if self.bullets > 0:
            self.bullets -= 1
            message = "shooting..."
        elif self.bullets == 0:
            message = "no bullets left"
        return message

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"