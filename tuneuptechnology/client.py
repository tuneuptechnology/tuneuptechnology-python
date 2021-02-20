import requests


class Client():
    VERSION = '2.1.0'
    API_BASE_URL = "https://app.tuneuptechnology.com/api/"

    @staticmethod
    def _make_http_request(data, endpoint):
        """Build the API request and return it to the method invoking it"""
        headers = {
            'User-Agent': f'TuneupTechnologyApp/PythonClient/{Client.VERSION}'
        }

        try:
            request = requests.post(
                endpoint,
                data=data,
                headers=headers,
                timeout=10,
            )
        except Exception as error:
            raise Exception(error)

        return request
