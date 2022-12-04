"""Create a class Movie. The __init__ method should receive a name and a director. It should also have a default value
of an attribute called watched set to False. There should also be a class attribute __watched_movies which will keep
track of the number of all the watched movies. The class should have the following methods:

· change_name(new_name: str) - changes the name of the movie
· change_director(new_director: str) - changes the director of the movie
· watch() - change the watched attribute to True and increase the total watched movies class attribute
(if the movie is not already watched)
· __repr__() - returns "Movie name: {name}; Movie director: {director}. Total watched movies: {__watched_movies}"""


class Movie:
    __watched_movies = []
    watched = False

    def __init__(self, name, director):
        self.name = name
        self.director = director

    def change_name(self, new_name):
        self.name = new_name

    def change_director(self, new_director):
        self.director = new_director

    def watch(self):
        if self.name not in Movie.__watched_movies:
            Movie.watched = True
            Movie.__watched_movies.append(self.name)

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {len(Movie.__watched_movies)}"