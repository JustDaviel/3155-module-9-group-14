from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_home_page(test_app: FlaskClient):
    repo = get_movie_repository()
    test_movie = repo.create_movie('MythBusters', 'Adam Savage', 99)

    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')

    has_title = '<th scope="col">MythBusters</th>' in response_data
    has_rating = '<th scope="col">99</th>' in response_data
    has_director = '<th scope="col">Adam Savage</th>' in response_data

    assert has_title and has_rating and has_director

    repo.delete_movie(test_movie.movie_id)
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')

    has_title = '<th scope="col">MythBusters</th>' in response_data
    has_rating = '<th scope="col">99</th>' in response_data
    has_director = '<th scope="col">Adam Savage</th>' in response_data

    assert not has_title and not has_rating and not has_director