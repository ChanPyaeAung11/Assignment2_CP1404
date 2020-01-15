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
    new_movie = []
    title = input("Movie title: ")
    new_movie.append(title)
    year = input("Year Released: ")
    new_movie.append(year)
    category = input("Genre: ")
    new_movie.append(category)
    new_movie.append("u")
    print(new_movie)
    movie_collection.add_movie(new_movie)
    print(movie_collection)

    # Test sorting movies
    """
    print("Test sorting - year:")
    movie_collection.sort("year")
    print(movie_collection)
    """
    # TODO: Add more sorting tests

    # TODO: Test saving movies (check CSV file manually to see results)

    # TODO: Add more tests, as appropriate, for each method


run_tests()
