"""Create a class called Book. It should have an __init__() method that should receive:
    -name: string
    -author: string
    -pages: int
Submit only the class in the judge system. """

class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages