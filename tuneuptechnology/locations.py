from typing import Callable

import requests


class Locations:
    def __init__(self, base_url: str, make_http_request: Callable):
        self.base_url = base_url
        self.make_http_request = make_http_request

    def create(self, data: dict) -> requests.Response:
        """Create a location based on the data passed."""
        endpoint = f'{self.base_url}/locations'
        response = self.make_http_request('post', endpoint, data)

        return response

    def all(self) -> requests.Response:
        """Retrieve all locations."""
        endpoint = f'{self.base_url}/locations'
        response = self.make_http_request('get', endpoint)

        return response

    def retrieve(self, id: str) -> requests.Response:
        """Retrieve a single location."""
        endpoint = f'{self.base_url}/locations/{id}'
        response = self.make_http_request('get', endpoint)

        return response

    def update(self, id: str, data: dict) -> requests.Response:
        """Update a location with the passed params."""
        endpoint = f'{self.base_url}/locations/{id}'
        response = self.make_http_request('patch', endpoint, data)

        return response

    def delete(self, id: str) -> requests.Response:
        """Delete a location with the ID passed."""
        endpoint = f'{self.base_url}/locations/{id}'
        response = self.make_http_request('delete', endpoint)

        return response
