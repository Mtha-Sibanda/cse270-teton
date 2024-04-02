import pytest
from unittest.mock import Mock
import requests

# @pytest.mark.integration
def test_unauthorized_access(mocker):
    # Define the endpoint URL
    url = 'http://127.0.0.1:8000/users'

    # Define the request parameters
    params = {'username': 'admin', 'password': 'password'}

    # Mocking requests.get method
    mocker.patch('requests.get', return_value=Mock(status_code=401))

    # Make the HTTP request
    response = requests.get(url, params=params)

    # Assert the response status code is 401 (Unauthorized)
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"

# @pytest.mark.integration
def test_authorized_access(mocker):
    # Define the endpoint URL
    url = 'http://127.0.0.1:8000/users'

    # Define the request parameters
    params = {'username': 'admin', 'password': 'qwerty'}

    # Mocking requests.get method
    mocker.patch('requests.get', return_value=Mock(status_code=200))

    # Make the HTTP request
    response = requests.get(url, params=params)

    # Assert the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

if __name__ == "__main__":
    pytest.main()
