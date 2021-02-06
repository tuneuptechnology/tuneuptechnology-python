import os

import tuneuptechnology

API_EMAIL = os.getenv('API_EMAIL')
API_KEY = os.getenv('API_KEY')

# Retrieve a single customer record
customer = tuneuptechnology.Customer.delete(
    data={
        'auth': API_EMAIL,
        'api_key': API_KEY,
        'id': 23  # the ID of the customer you are deleting
    }
)

tuneuptechnology.Util.pretty_print(customer)
