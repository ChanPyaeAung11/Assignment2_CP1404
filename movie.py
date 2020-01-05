"""
Name: Chan Pyae Aung
Date Started: 5 Jan 2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-02-ChanPyaeAung11
"""


class Movie:

    def __init__(self, name, year, cateogry, watched):
        """ use parameters pass =ed in this and construct them"""
        self.name = name
        self.year = year
        self.category = cateogry
        self.watched = watched

    def __str__(self):
        """ return strings about movie details"""
        return "{}, {}, {}, {}".format(self.name, self.year, self.category, self.watched)
