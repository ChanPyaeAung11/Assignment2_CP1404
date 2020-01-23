"""
Name: Chan Pyae Aung
Date Started: 5 Jan 2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-02-ChanPyaeAung11
"""
from movie import Movie


class MovieCollection:
    """ classes to be used in main.py for movies app"""

    def __str__(self):  # for testing
        """ print out the movies list"""
        return "Movies :{}".format(self.movies)

    def __init__(self):
        """ construct things needed for the class and initiate watched and unwatched movies"""
        self.movies = []
        self.unwatch_movie = ''
        self.watch_movie = ''

    def add_movie(self, new_movie):
        """ function to add new movies to the movies list"""
        self.movies.append(new_movie)

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

    def load_movies(self, file):
        """ load movies from the file and load them into the movies list """
        with open(file, 'r') as csv:
            for line in csv.readlines():
                title, year, category, is_watched = line.replace("\n", "").split(",")
                is_watched = is_watched == "w"
                i = Movie(title, year, category, is_watched)
                self.movies.append(i)  # add the movie data into the list

    def save_file(self, output_file="movies.csv"):
        """to write the list of data into the csv file"""
        with open(output_file, 'w') as csv:
            for movie in self.movies:
                csv.write(movie.save_movie())
        csv.close()

    def sort_movie(self, sort_by):
        """to sort the movie based on given types"""
        self.movies.sort(key=lambda i: getattr(i, sort_by))
