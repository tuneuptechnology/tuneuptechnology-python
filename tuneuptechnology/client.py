import requests

VERSION = '2.1.0'
API_BASE_URL = "https://app.tuneuptechnology.com/api/"


class Client():
    @staticmethod
    def response(data, endpoint):
        """Build the API request and return it to the method invoking it"""
        headers = {
            'User-Agent': f'TuneupTechnologyApp/PythonClient/{VERSION}'
        }
        request = requests.post(
            endpoint,
            data=data,
            headers=headers,
        )
        return request
