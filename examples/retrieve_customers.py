import os

import tuneuptechnology

API_EMAIL = os.getenv('API_EMAIL')
API_KEY = os.getenv('API_KEY')

customers = tuneuptechnology.Customer.all(
    data={
        'auth': API_EMAIL,
        'api_key': API_KEY,
    }
)

tuneuptechnology.Util.pretty_print(customers)
