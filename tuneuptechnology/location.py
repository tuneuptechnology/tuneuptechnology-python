from tuneuptechnology.client import Client


class Location(Client):
    @staticmethod
    def create(data):
        """Create a location based on the data passed"""
        endpoint = f'{Client.API_BASE_URL}locations/create'
        response = Client._make_http_request(data, endpoint)
        return response.json()

    @staticmethod
    def all(data):
        """Retrieve all locations"""
        endpoint = f'{Client.API_BASE_URL}locations'
        response = Client._make_http_request(data, endpoint)
        return response.json()

    @staticmethod
    def retrieve(data):
        """Retrieve a single location"""
        endpoint = f'{Client.API_BASE_URL}locations/{data["id"]}'
        response = Client._make_http_request(data, endpoint)
        return response.json()

    @staticmethod
    def update(data):
        """Update a location with the passed params"""
        endpoint = f'{Client.API_BASE_URL}locations/{data["id"]}/update'
        response = Client._make_http_request(data, endpoint)
        return response.json()

    @staticmethod
    def delete(data):
        """Delete a location with the ID passed"""
        endpoint = f'{Client.API_BASE_URL}locations/{data["id"]}/delete'
        response = Client._make_http_request(data, endpoint)
        return response.json()
