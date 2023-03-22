# TODO: Feature 2
from src.models.movie import Movie
def test_create_movie():
    movie = Movie('John Wick', 'Len Wiseman', 7.0)
    assert movie
