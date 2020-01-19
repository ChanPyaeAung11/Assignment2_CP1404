"""
Name: Chan Pyae Aung
Date Started: 5 Jan 2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-02-ChanPyaeAung11
"""

from movie import Movie
from moviecollection import MovieCollection

# import itemgetter to sort the list according to year
from operator import itemgetter

# constants are put here so that I dont need to repeat writing them in the program
MENU = "MENU: \n \t L - List movies \n \t A - Add new movie \n \t W - Watch a movie \n \t Q - Quit"

# constance, a list of choices which will later be used to error check users input
choice = ["l", "q", "a", "w"]


# this is the main function from which user can choose what function to do.
# watch movie or add new movies or ask for the lists of movies or even quit the program.
# menu will be repeated asked until user quit the program
def main():
    print("Movies To Watch 1.0 - by Chan Pyae Aung")
    taken_movies = file_reading()  # this calls file_reading function which read the file and put to the list
    print(len(taken_movies), "movies loaded")
    while True:
        print(MENU)  # prints out menu which is a constant from above
        menu_cho = input(">>> ".lower())
        while menu_cho not in choice:  # error checking whether user input menu choices that are (l or q or a or w)
            print("Invalid Input")
            menu_cho = input(">>> ".lower())
        if menu_cho == "l":
            movie_listin(taken_movies)  # put taken_movies list and calls movie_listin function
        elif menu_cho == "w":
            # all_movies_watched function checks whether all movies are watched or not,
            # it goes into watch_movie function
            watch_movie(taken_movies, all_movies_watched(taken_movies))
        elif menu_cho == "a":
            taken_movies.append(add_movie())  # calls add_movie function and append the list to taken_movies list
            taken_movies.sort(key=itemgetter(1, 0))  # sort out the list according to year
        else:
            # gives taken_movies list and calls file_save function
            print(file_save(taken_movies), "saved to movies.csv")
            print("Have a nice day :)")
            exit()          # exits the whole program


# read the file and put movies into lists of lists
def file_reading():
    movie_list = []
    actual = []
    movie_file = open("movies.csv", "r")

    for i in movie_file:
        movie_list.append(i.strip('\n'))

    for j in movie_list:
        actual.append(j.split(','))         # the list that will be used throughout the program
    actual.sort(key=itemgetter(1, 0))       # sorting the list according to year and name
    movie_file.close()
    return actual


# function to print movies from the list and decide whether to put * or none
def movie_listin(taken_movies):
    k = -1
    u_count = 0
    w_count = 0
    for m in taken_movies:
        k += 1
        if m[3] == "u":
            u_count += 1
            print(k, ". * {:40} {:>10} ({:>4})".format(m[0], m[1], m[2]))
        else:
            w_count += 1
            print(k, ".   {:40} {:>10} ({:>4})".format(m[0], m[1], m[2]))
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

    print(movie_name, "(" "{} from {}".format(cate, year),")", "is added to movie list.")
    return new_movie


# function to check whether all movies are watched or not.
# if all movies are watched, function returns True
# if not, function returns False
def all_movies_watched(taken_movies):
    for movie in taken_movies:
        if movie[3] == "u":
            return False
    return True


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
        while ask > len(taken_movies) - 1 or ask < 0:  # error checking user input
            print("This does not exist. Choose Again.")
            ask = valid_int(">>> ")
        if taken_movies[ask][3] == 'u':
            taken_movies[ask][3] = 'w'  # changes the 'u' to 'w' to indicate as watched
            print(taken_movies[ask][0] + " from " + taken_movies[ask][1] + " watched.")
        else:
            print("You have already watched " + taken_movies[ask][0] + ".")
    return taken_movies


# this function overwrites the final lists of lists to the file
# final_count is counting numbers of movies and returned to main.
def file_save(taken_movies):
    final_count = 0
    movie_file = open("movies.csv", "w")
    for data in taken_movies:
        movie_file.writelines(','.join(data) + "\n")
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

