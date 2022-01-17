from typing import Callable

import requests


class Inventory:
    def __init__(self, base_url: str, make_http_request: Callable):
        self.base_url = base_url
        self.make_http_request = make_http_request

    def create(self, data: dict) -> requests.Response:
        """Create an inventory item based on the data passed."""
        endpoint = f'{self.base_url}/inventory'
        response = self.make_http_request('post', endpoint, data)

        return response

    def all(self) -> requests.Response:
        """Retrieve all inventory."""
        endpoint = f'{self.base_url}/inventory'
        response = self.make_http_request('get', endpoint)

        return response

    def retrieve(self, id: str) -> requests.Response:
        """Retrieve a single inventory item."""
        endpoint = f'{self.base_url}/inventory/{id}'
        response = self.make_http_request('get', endpoint)

        return response

    def update(self, id: str, data: dict) -> requests.Response:
        """Update an inventory item with the passed params."""
        endpoint = f'{self.base_url}/inventory/{id}'
        response = self.make_http_request('patch', endpoint, data)

        return response

    def delete(self, id: str) -> requests.Response:
        """Delete an inventory item with the ID passed."""
        endpoint = f'{self.base_url}/inventory/{id}'
        response = self.make_http_request('delete', endpoint)

        return response
