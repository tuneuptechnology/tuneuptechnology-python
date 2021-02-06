import os

import tuneuptechnology

API_EMAIL = os.getenv('API_EMAIL')
API_KEY = os.getenv('API_KEY')

customer = tuneuptechnology.Customer.update(
    data={
        'auth': API_EMAIL,
        'api_key': API_KEY,
        'id': 23,  # the ID of the customer you are updating
        'firstname': 'Jake',
        'lastname': 'Peralta',
        'email': 'jake@example.com',
        'phone': '8015551234',
        'user_id': 1,
        'notes': 'Believes he is a good detective.',
        'location_id': 1,
    }
)

tuneuptechnology.Util.pretty_print(customer)
