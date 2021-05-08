import os

import tuneuptechnology

API_EMAIL = os.getenv('API_EMAIL')
API_KEY = os.getenv('API_KEY')

client = tuneuptechnology.Client(API_EMAIL, API_KEY)

customer = client.Customers.update(
    id=23,
    data={
        'firstname': 'Jake',
        'lastname': 'Peralta',
        'email': 'jake@example.com',
        'phone': '8015551234',
        'user_id': 1,
        'notes': 'Believes he is a good detective.',
        'location_id': 2,
    }
)

print(customer.json())
