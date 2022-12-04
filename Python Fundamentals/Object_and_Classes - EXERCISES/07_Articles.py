"""Create a class called Article. The __init__ method should accept 3 arguments: title: str, content: str, and author:
str. The class should also have 4 methods:

· edit(new_content: str) - changes the old content to the new one
· change_author(new_author: str) - changes the old author with the new one
· rename(new_title: str) - changes the old title with the new one
· __repr__() - returns the following string "{title} - {content}: {author}"""


class Article:

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content):
        self.content = new_content

    def change_author(self, new_author):
        self.author = new_author

    def rename(self, new_title):
        self.title = new_title

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"