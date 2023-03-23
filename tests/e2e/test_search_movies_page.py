from flask import Response
from app import app
from src.repositories.movie_repository import get_movie_repository


random_movie_repo = get_movie_repository()

random_movie_repo.create_movie('Star Wars: The Force Awakens', 'A Director Guy', 2)
random_movie_repo.create_movie('Spider Man: No Way Home', 'Director Name', 4)
random_movie_repo.create_movie('The Bee Movie', 'Buzzy Director', 5)

def test_search_movies_page(test_app):
  
    response = test_app.get('movies/search', data={'movie-title': 'Star Wars: The Force Awakens'})
    assert response.status_code == 200

    response = test_app.post('movies/search', data={'movie-title': 'Star Wars: The Force Awakens'})
    assert response.status_code == 200

    response = test_app.get('movies/search', data={'movie-title': 'Star Wars: The Force Awakens'})
    assert response.status_code == 200
    data = response.data.decode('utf-8')

    assert '<p class="mb-3">Zero Movies Found</p>' in data




  



