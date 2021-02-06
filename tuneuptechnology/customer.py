from tuneuptechnology.client import Client


class Customer(Client):
    @staticmethod
    def create(data):
        """Create a customer based on the data passed"""
        endpoint = f'{Client.API_BASE_URL}customers/create'
        response = Client.response(data, endpoint)
        return response.json()

    @staticmethod
    def all(data):
        """Retrieve all customers"""
        endpoint = f'{Client.API_BASE_URL}customers'
        response = Client.response(data, endpoint)
        return response.json()

    @staticmethod
    def retrieve(data):
        """Retrieve a single customer"""
        endpoint = f'{Client.API_BASE_URL}customers/{data["id"]}'
        response = Client.response(data, endpoint)
        return response.json()

    @staticmethod
    def update(data):
        """Update a customer with the passed params"""
        endpoint = f'{Client.API_BASE_URL}customers/{data["id"]}/update'
        response = Client.response(data, endpoint)
        return response.json()

    @staticmethod
    def delete(data):
        """Delete a customer with the ID passed"""
        endpoint = f'{Client.API_BASE_URL}customers/{data["id"]}/delete'
        response = Client.response(data, endpoint)
        return response.json()
