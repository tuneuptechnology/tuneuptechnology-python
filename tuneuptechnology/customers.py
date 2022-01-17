from typing import Callable

import requests


class Customers:
    def __init__(self, base_url: str, make_http_request: Callable):
        self.base_url = base_url
        self.make_http_request = make_http_request

    def create(self, data: dict) -> requests.Response:
        """Create a customer based on the data passed."""
        endpoint = f'{self.base_url}/customers'
        response = self.make_http_request('post', endpoint, data)

        return response

    def all(self) -> requests.Response:
        """Retrieve all customers."""
        endpoint = f'{self.base_url}/customers'
        response = self.make_http_request('get', endpoint)

        return response

    def retrieve(self, id: str) -> requests.Response:
        """Retrieve a single customer."""
        endpoint = f'{self.base_url}/customers/{id}'
        response = self.make_http_request('get', endpoint)

        return response

    def update(self, id: str, data: dict) -> requests.Response:
        """Update a customer with the passed params."""
        endpoint = f'{self.base_url}/customers/{id}'
        response = self.make_http_request('patch', endpoint, data)

        return response

    def delete(self, id: str) -> requests.Response:
        """Delete a customer with the ID passed."""
        endpoint = f'{self.base_url}/customers/{id}'
        response = self.make_http_request('delete', endpoint)

        return response
