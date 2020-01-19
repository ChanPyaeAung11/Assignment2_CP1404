"""
Name: Chan Pyae Aung
Date Started: 5 Jan 2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-02-ChanPyaeAung11
"""
from movie import Movie

class MovieCollection:

    def __init__(self):
        """ construct things needed for the class"""
        self.movies = []
        self.unwatch_movie = ''
        self.watch_movie = ''

    def __str__(self):
        """ print out the movies list"""
        return "Movies :{}".format(self.movies)

    def load_movies(self, csv):
        """ load movies from the file and load them into the movies list """
        with open(csv, 'r') as csv:
            for line in csv.readlines():
                title, year, category, is_watched = line.replace("\n", "").split(",")
                is_watched = is_watched == "w"
                i = Movie(title, year, category, is_watched)
                self.movies.append(i)

    def add_movie(self, new_movie):
        """ function to add new movies to the movies list"""
        self.movies.append(new_movie)
        return self.movies

    def get_unwatched_movies(self):
        """ function to get numbers of unwatched movies"""
        self.unwatch_movie = ''
        left = len([movie for movie in self.movies if not movie.is_watched])
        self.unwatch_movie = left

    def get_watched_movies(self):
        """ function to get numbers of watched movies"""
        self.watch_movie = ''
        right = len([movie for movie in self.movies if movie.is_watched])
        self.watch_movie = right

    def sort_movies(self, sort_by):
        """ sort movies according to given types"""
        self.movies.sort(key=lambda x: getattr(x, sort_by))

    def save_file(self, csv):
        """ saves the final list into the file """
        with open(csv, 'w'):
            for movie in self.movies:
                csv.write(movie.save_csv())

