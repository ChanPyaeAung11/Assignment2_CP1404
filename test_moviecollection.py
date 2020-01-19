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
    assert movie_collection.movies  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Movie with values
    print("Test adding new movie:")
    test_new_movie = ["Cats", 2019, "Musical", "u"]
    assert test_new_movie[0] == "Cats"
    assert test_new_movie[1] == 2019
    assert test_new_movie[2] == "Musical"
    assert test_new_movie[3] == "u"
    movie_collection.add_movie(test_new_movie)
    print(movie_collection)

    # Test sorting movies

    print("Test sorting - year:")
    movie_collection.sort_movies("year")
    print(movie_collection)
    # TODO: Add more sorting tests

    print("Test saving movies into the file")
    movie_collection.save_file('movies.csv')

    # Test to get number of unwatched movies
    print("Test getting number of unwatched movies:")
    unwatched_movies = movie_collection.get_unwatched_movies()
    assert not unwatched_movies < 0
    assert unwatched_movies >= 0
    print(unwatched_movies)

    # Test to get number of watched movies
    print("Test getting number of watched movies:")
    watched_movies = movie_collection.get_watched_movies()
    assert not watched_movies < 0
    assert watched_movies <= 0
    print(watched_movies)


run_tests()
