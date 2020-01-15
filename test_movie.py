"""(Incomplete) Tests for Movie class."""
from movie import Movie


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie()
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert not default_movie.is_watched

    # Test initial-value movie
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", "w")
    print(initial_movie)
    # Test whether check_unwatched and check_watched function works and return what they are supposed to
    if initial_movie.check_unwatched():
        initial_movie.is_watched = False
    elif initial_movie.check_watched():
        initial_movie.is_watched = True
    print(initial_movie)


run_tests()
