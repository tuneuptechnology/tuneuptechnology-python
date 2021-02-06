import os

import tuneuptechnology

API_EMAIL = os.getenv('API_EMAIL')
API_KEY = os.getenv('API_KEY')

customer = tuneuptechnology.Customer.retrieve(
    data={
        'auth': API_EMAIL,
        'api_key': API_KEY,
        'id': 23  # the ID of the customer you are retrieving
    }
)

tuneuptechnology.Util.pretty_print(customer)
