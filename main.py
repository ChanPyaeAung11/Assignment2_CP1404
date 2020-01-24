"""
Name: Chan Pyae Aung
Date Started: 5 Jan 2020
Brief Project Description: Create a small kivy interfaced program that let users play around with the movies.csv
GitHub URL: https://github.com/JCUS-CP1404/assignment-02-ChanPyaeAung11
"""

# import modules that will be used in the program
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from moviecollection import MovieCollection
from kivy.app import App
from movie import Movie

# colors for buttons which are constants which is why written above
COLORS = [[0, 230, 250, 0.5], [0.988,0.0117,0.0117,1]]
# this is for sorting options
sorting = {'Title': 'title', 'Year': 'year', 'Category': 'category',
           'Watched': 'is_watched'}


class MoviesToWatchApp(App):
    """ Kivy app for movie app"""
    display_sort = StringProperty()
    sort_type = ListProperty()

    def display_sorting(self, text):
        """ show sorting based on the user want"""
        self.current_display_sorting = text
        self.show_movie()

    def __init__(self):
        """ construct things needed for class"""
        self.movie_collection = MovieCollection()  # call movie collection
        self.movie_collection.load_movies('movies.csv')  # to open csv file
        self.movie_collection.get_unwatched_movies()  # getting the number of unwatched movies
        self.movie_collection.get_watched_movies()  # getting the number watch movies
        self.num_of_unwatch = self.movie_collection.unwatch_movie  # count unwatched movies
        self.num_of_watch = self.movie_collection.watch_movie  # count watched movie
        self.movie_dict = {movie.title: movie for movie in self.movie_collection.movies}  # to initialize the dictionary
        self.btn_movie = []  # list data for button
        self.sorting_type = list(sorting.keys())  # sorting type
        self.current_display_sorting = self.sorting_type[+2]  # set default sorting
        super().__init__()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Movie to Watch 2.0"  # title for the kivy app
        self.root = Builder.load_file('app.kv')  # opening kivy with file name
        self.show_movie()  # to show movies
        self.root.ids.status_watch.text = (
            "To watch: {}. Watched: {}".format(self.num_of_unwatch,
                                               self.num_of_watch))  # display how many movies watched and left to watch
        return self.root

    def sort_display(self, text):
        """display sorting based on the user want"""
        self.current_display_sorting = text
        self.show_movie()

    def clear(self):
        """ this is to clear data so that the previous movie not added again"""
        for value in self.btn_movie:
            self.root.ids.display_movie.remove_widget(value)

    def show_movie(self):
        """  displaying movies from list"""
        self.clear()  # clear the input value from widget
        self.movie_collection.sort_movie(sorting[self.current_display_sorting])
        self.btn_movie = []
        for movie in self.movie_collection.movies:
            color = COLORS[movie.is_watched]  # the color of the button
            text = "{} ({} from {})".format(movie.title, movie.category, movie.year)  # writing on button
            if movie.is_watched:  # if movie is watched, add this string
                text += " (Watched)"
            btn = Button(text=text, id=movie.title, background_color=color)
            btn.bind(on_release=self.change_watch)
            self.btn_movie.append(btn)
            self.root.ids.display_movie.add_widget(btn)

    def change_watch(self, instance):
        """ Change interfaces an texts on kivy when the users watch or not watch the movie"""
        watch = self.movie_dict[instance.id]
        if watch.is_watched:
            watch.check_unwatched()
            if watch.year_level():
                self.root.ids.message.text = ("You need to watch {}".format(watch.title))
            else:
                watch.check_unwatched()
                self.root.ids.message.text = ("You need to watch {}".format(watch.title))
        else:
            watch.check_watched()
            if watch.year_level():
                self.root.ids.message.text = ("You have watched {}".format(watch.title))
            else:
                watch.check_watched()
                self.root.ids.message.text = (
                    "you have watched {}.".format(watch.title))  # if the movie is watched, display this message
        self.movie_collection.get_unwatched_movies()  # get number of unwatched movies
        self.movie_collection.get_watched_movies()
        # update and display number of movie watched and need to watch
        self.root.ids.status_watch.text = ("To watch: {}. Watched: {}".format(self.movie_collection.unwatch_movie,
                                                                              self.movie_collection.watch_movie))
        instance.background_color = COLORS[watch.is_watched]  # change the button colour
        self.show_movie()  # display new buttons

    def add_movie(self):
        """ method to add new movies from users"""
        title = self.root.ids.title.text  # add input
        title = title.capitalize()
        year = self.root.ids.year.text
        category = self.root.ids.category.text
        error_check = self.error_checker()  # error check input
        # after error checking done
        if not error_check:
            m = Movie(title, year, category)  # add input to the list
            self.movie_collection.add_movie(m)
            self.movie_dict[title] = m  # add into the dictionary
            self.show_movie()
            self.movie_collection.get_unwatched_movies()  # to get update number of unwatched movie
            self.root.ids.status_watch.text = ("To watch: {}. Watched: {}".format(self.movie_collection.unwatch_movie,
                                                                                  self.movie_collection.watch_movie))
            self.clear_input_movie()  # clear input when the movie successfully added
            self.root.ids.message.text = ''  # check the input

    def error_checker(self):
        """ error checking user input"""
        error_check = False
        title = self.root.ids.title.text  # add input from the user
        title = title.capitalize()  # auto capitalize so the input will not interfere with sort
        category = self.root.ids.category.text
        category = category.capitalize()
        year = self.root.ids.year.text

        if category not in ('Action', 'Comedy', 'Documentary', 'Drama', 'Fantasy', 'Thriller'):
            # prevent user from entering invalid words other than categories
            self.root.ids.message.text = ('Category must be one of Action, Comedy,'
                                          ' Documentary, Drama, Fantasy, and Thriller')
            error_check = True
            return error_check
        if not (title and year and category):   # asks user to fill in all fields
            self.root.ids.message.text = 'All fields must be completed.'
            error_check = True
        elif not year.isdigit():  # prevents user from inputting things other than digits
            self.root.ids.message.text = 'Please enter a valid number.'
            error_check = True
        elif len(str(year)) < 4:  # prevent user inputting numbers less than 4 digits
            self.root.ids.message.text = 'Year must be 4 digits.'
            error_check = True
        return error_check

    def clear_input_movie(self):
        """ delete all user inputs when the user clicks clear button"""
        self.root.ids.title.text = ""
        self.root.ids.year.text = ""
        self.root.ids.category.text = ""

    def on_stop(self):
        """saves updated movies into the csv file"""
        self.movie_collection.save_file("movies.csv")


if __name__ == '__main__':
    MoviesToWatchApp().run()
