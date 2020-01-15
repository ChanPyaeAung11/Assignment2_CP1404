"""
Name: Chan Pyae Aung
Date Started: 5 Jan 2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-02-ChanPyaeAung11
"""


class MovieCollection:

    def __init__(self, movies=None):
        """ construct things needed for the class"""
        if movies is None:
            movies = []
        self.movies = movies

    def __str__(self):
        """ print out the movies list"""
        return "Movies :{}".format(self.movies)

    def load_movies(self, csv):
        """ load movies from the file and load them into the movies list """
        load_file = open(csv, "r")
        for line in load_file:
            if not line.strip():
                continue
            else:
                self.movies.append(line)
        self.movies = [line.strip('\n') for line in self.movies]
        self.movies = [line.split(",") for line in self.movies]

    def add_movie(self, new_movie):
        """ function to add new movies to the movies list"""
        self.movies.append(new_movie)
        return self.movies

    def get_unwatched_movies(self):
        """ function to get numbers of unwatched movies"""
        unwatched_movies = 0
        for i in range(len(self.movies)):
            if self.movies[i][3] == "u":
                unwatched_movies += 1
        return unwatched_movies

    def get_watched_movies(self, unwatched_movies):
        """ function to get numbers of watched movies"""
        print(unwatched_movies)
        watched_movies = len(self.movies) - unwatched_movies
        return watched_movies
    pass
