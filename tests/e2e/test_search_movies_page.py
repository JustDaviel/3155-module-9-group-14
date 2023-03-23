from flask import Response
from app import app
from src.repositories.movie_repository import get_movie_repository


random_movie_repo = get_movie_repository()
client_user = app.test_client

random_movie_repo.create_movie('Star Wars: The Force Awakens', 'A Director Guy', 2)
random_movie_repo.create_movie('Spider Man: No Way Home', 'Director Name', 4)
random_movie_repo.create_movie('The Bee Movie', 'Buzzy Director', 5)

def test_search_movies_page():
  
    response = client_user.get('movies/search', data={'movie-title': 'Star Wars: The Force Awakens'})
assert Response.status_code == 200

response = client_user.post('movies/search', data={'movie-title': 'Star Wars: The Force Awakens'})
assert response.status_code == 200

response = client_user.get('movies/search', data={'movie-title': 'Star Wars: The Force Awakens'})
assert response.status_code == 200
data = response.data.decode('utf-8')

assert '<p class="mb-3"></p>' in data




  



