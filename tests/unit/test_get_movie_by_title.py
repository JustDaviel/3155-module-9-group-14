from src.repositories.movie_repository import get_movie_repository


random_movie_repo = get_movie_repository()

random_movie_repo.create_movie('Star Wars: The Force Awakens', 'A Director Guy', 2)
random_movie_repo.create_movie('Spider Man: No Way Home', 'Director Name', 4)
random_movie_repo.create_movie('The Bee Movie', 'Buzzy Director', 5)

def test_get_movie_by_title():

# testing for a movie that exists
    assert random_movie_repo.get_movie_by_title('The Bee Movie')

# testing for a movie that doesnt exist
    assert random_movie_repo.get_movie_by_title('The Iron Giant') == None
