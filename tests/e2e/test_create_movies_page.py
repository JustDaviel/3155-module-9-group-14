# TODO: Feature 2
from app import movie_repository
from flask.testing import FlaskClient
def test_create_movie(test_app: FlaskClient):
    movie_repository.create_movie('Scary Movie 2','Keenen Ivory Wayans','3')
    response = test_app.post('/movies')
    assert response
