from tuneuptechnology.client import Client


class Inventory(Client):
    @staticmethod
    def create(data):
        """Create an inventory item based on the data passed"""
        endpoint = f'{Client.API_BASE_URL}inventory/create'
        response = Client._make_http_request(data, endpoint)
        return response.json()

    @staticmethod
    def all(data):
        """Retrieve all inventory"""
        endpoint = f'{Client.API_BASE_URL}inventorys'
        response = Client._make_http_request(data, endpoint)
        return response.json()

    @staticmethod
    def retrieve(data):
        """Retrieve a single inventory item"""
        endpoint = f'{Client.API_BASE_URL}inventory/{data["id"]}'
        response = Client._make_http_request(data, endpoint)
        return response.json()

    @staticmethod
    def update(data):
        """Update an inventory item with the passed params"""
        endpoint = f'{Client.API_BASE_URL}inventory/{data["id"]}/update'
        response = Client._make_http_request(data, endpoint)
        return response.json()

    @staticmethod
    def delete(data):
        """Delete an inventory item with the ID passed"""
        endpoint = f'{Client.API_BASE_URL}inventory/{data["id"]}/delete'
        response = Client._make_http_request(data, endpoint)
        return response.json()
