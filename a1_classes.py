"""
Name: Chan Pyae Aung
Date Started: 5 Jan 2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-02-ChanPyaeAung11
"""
from movie import Movie     # import classes from moviecollection.py and movie.py
from operator import itemgetter  # import itemgetter to sort the list according to year

"""CONSTANTS are put here so that I dont need to repeat writing them in the program """
MENU = "MENU: \n \t L - List movies \n \t A - Add new movie \n \t W - Watch a movie \n \t Q - Quit"
choice = ["l", "q", "a", "w"]  # a list of choices which will later be used to error check users input

csv_data = []
movie_data = []
csv = 'movies.csv'
load_file = open(csv, "r")
for line in load_file:
    if not line.strip():
        continue
    else:
        csv_data.append(line)
movies = [line.strip('\n') for line in csv_data]
for line in movies:  # making movies data store as an object
    title, year, category, is_watched = line.split(',')
    is_watched = is_watched == 'w'
    name_parts = Movie(title, year, category, is_watched)
    movie_data.append(name_parts)


def main():
    print("Movies To Watch 1.0 - by Chan Pyae Aung")
    print(len(movie_data), "movies loaded")
    while True:
        print(MENU)  # prints out menu which is a constant from above
        menu_choice = input(">>> ".lower())
        while menu_choice not in choice:  # error checking whether user input menu choices that are (l or q or a or w)
            print("Invalid Input")
            menu_choice = input(">>> ".lower())
        if menu_choice == "l":
            movie_listing()  # put taken_movies list and calls movie_listin function
        elif menu_choice == "w":
            # all_movies_watched function checks whether all movies are watched or not,
            # it goes into watch_movie function
            watch_movie(movie_data, all_movies_watched(movie_data))
        elif menu_choice == "a":
            movie_data.append(add_movie())  # calls add_movie function and append the list to taken_movies list
            movie_data.sort(key=itemgetter(1, 0))  # sort out the list according to year
        else:
            # gives taken_movies list and calls file_save function
            print(save_file(), "saved to movies.csv")
            print("Have a nice day :)")
            exit()  # exits the whole program


# function to print movies from the list and decide whether to put * or none
def movie_listing():
    k = -1
    u_count = 0
    w_count = 0
    for m in range(len(movie_data)):
        k += 1
        if not movie_data[m].is_watched:
            u_count += 1
            print(k, ". * {:40} {:>10} ({:>4})".format(movie_data[m].title, movie_data[m].year, movie_data[m].category))
        else:
            w_count += 1
            print(k, ".   {:40} {:>10} ({:>4})".format(movie_data[m].title, movie_data[m].year, movie_data[m].category))
    print(u_count, " movies to watch, ", w_count, " still to watch")


# function ask for new movies names, year and category, error checking each input and put them into the list
# returns the new movie list to main
def add_movie():
    new_movie = []
    movie_name = input("Movie Name:")
    while movie_name == "":  # error check so that user cannot input blanks
        print("This cannot be blank")
        movie_name = input("Movie Name:")
    new_movie.append(movie_name)

    year = valid_int("Release Year: ")  # calls valid_int function to error check integer input
    while year <= 0:
        print("Number must be positive")
        year = valid_int("Release Year: ")
    # put 0s in front of integers that have less than 4 digits
    if len(str(year)) < 4:
        if len(str(year)) == 3:
            year = '0' + str(year)
        elif len(str(year)) == 2:
            year = '00' + str(year)
        elif len(str(year)) == 1:
            year = '000' + str(year)
    else:
        new_movie.append(str(year))

    cate = input("Movie category: ")
    while not cate:  # error check so that user cannot input blanks
        print("This cannot be blank")
        cate = input("Movie category: ")
    new_movie.append(cate)

    new_movie.append("u")

    print(movie_name, "(" "{} from {}".format(cate, year), ")", "is added to movie list.")
    return new_movie


# function to check whether all movies are watched or not.
# if all movies are watched, function returns True
# if not, function returns False
def all_movies_watched(movie_data):
    for movie in movie_data:
        if movie.check_watched():
            return True
    return False


# this function first takes True or False from all_movies_watched and movies lists of lists
# if True, print out "cannot watch anything."
# if False, ask for which movie to watch
# and mark "w" beside that movie.
# if a movie watched is chosen, print out that this movie is already watched.
# then, returns the lists of lists as updated
def watch_movie(taken_movies, movie_watched):
    if movie_watched is True:
        print("no more movies to watch")
    else:
        print("Enter the number of a movie to mark as watched")
        ask = valid_int(">>> ")
        while ask > len(taken_movies) - 2 or ask < 0:  # error checking user input
            print("This does not exist. Choose Again.")
            ask = valid_int(">>> ")
        if not taken_movies[ask].is_watched:
            taken_movies[ask].is_watched = True  # changes the 'u' to 'w' to indicate as watched
            print(taken_movies[ask].title + " from " + taken_movies[ask].year + " watched.")
        else:
            print("You have already watched " + taken_movies[ask].title + ".")
    return taken_movies


# this function overwrites the final lists of lists to the file
# final_count is counting numbers of movies and returned to main.
def save_file():
    final_count = 0
    movie_file = open("movies.csv", "w")
    for data in movie_data:
        movie_file.write(data.save_movie())
        final_count += 1
    movie_file.close()
    return final_count


# this function is for error checking integer input.
# this is used in add_movie()
# this function will loop until user input integer.
def valid_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please enter a valid integer")


if __name__ == '__main__':
    main()
