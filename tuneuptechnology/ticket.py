from tuneuptechnology.client import Client


class Ticket(Client):
    @staticmethod
    def create(data):
        """Create a ticket based on the data passed"""
        endpoint = f'{Client.API_BASE_URL}tickets/create'
        response = Client.response(data, endpoint)
        return response.json()

    @staticmethod
    def all(data):
        """Retrieve all tickets"""
        endpoint = f'{Client.API_BASE_URL}tickets'
        response = Client.response(data, endpoint)
        return response.json()

    @staticmethod
    def retrieve(data):
        """Retrieve a single ticket"""
        endpoint = f'{Client.API_BASE_URL}tickets/{data["id"]}'
        response = Client.response(data, endpoint)
        return response.json()

    @staticmethod
    def update(data):
        """Update a ticket with the passed params"""
        endpoint = f'{Client.API_BASE_URL}tickets/{data["id"]}/update'
        response = Client.response(data, endpoint)
        return response.json()

    @staticmethod
    def delete(data):
        """Delete a ticket with the ID passed"""
        endpoint = f'{Client.API_BASE_URL}tickets/{data["id"]}/delete'
        response = Client.response(data, endpoint)
        return response.json()
