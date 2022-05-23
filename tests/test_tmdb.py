from unittest.mock import Mock
import tmdb_client


def test_get_poster_url_uses_default_size():
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   assert expected_default_size in poster_url

def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None

def test_get_single_movie_cast_how_many():
    cast = tmdb_client.get_single_movie_cast(movie_id=725273, how_many=3)
    assert len(cast)==3


def test_get_movies_list(monkeypatch):
   mock_movies_list = ['Movie 1', 'Movie 2']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_single_movie_cast(monkeypatch):
   mock_single_movie_cast = {"cast": []}
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   cast = tmdb_client.get_single_movie_cast(movie_id=725273, how_many=2)
   assert cast == mock_single_movie_cast["cast"]

def test_get_single_movie(monkeypatch):
    mock_single_movie = ["Movie 1"]
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movie = tmdb_client.get_single_movie(movie_id=725273)
    assert movie == mock_single_movie

def test_get_movie_images(monkeypatch):
    mock_movies_images = ['Movie 1', 'Movie 2']
    requests_mock = Mock()
    responce = requests_mock.return_value
    responce.json.return_value = mock_movies_images
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_images = tmdb_client.get_movie_images(movie_id=1)
    assert movies_images == mock_movies_images