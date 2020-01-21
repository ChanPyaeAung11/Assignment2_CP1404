"""(Incomplete) Tests for MovieCollection class."""
from movie import Movie
from moviecollection import MovieCollection


def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert not movie_collection.movies  # an empty list is considered False

    # Test loading movies
    print("Test loading movies:")
    movie_collection.load_movies('movies.csv')
    print(movie_collection)
    assert movie_collection.movies

    # Test adding a new Movie with values
    print("Test adding new movie:")
    movie_collection.add_movie(Movie("Cats", 2019, "Musical", "u"))     # adding new movies
    print(movie_collection)

    # Test sorting movies

    print("Test sorting - year:")
    movie_collection.sort_movie("year")
    print(movie_collection)

    # Test to get number of unwatched movies
    print("Test getting number of unwatched movies:")
    unwatched_movies = movie_collection.get_unwatched_movies()
    print(unwatched_movies)

    # Test to get number of watched movies
    print("Test getting number of watched movies:")
    watched_movies = movie_collection.get_watched_movies()
    print(watched_movies)

    print("Test saving movies into the file")
    movie_collection.save_file('movies.csv')


run_tests()
