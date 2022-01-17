import os

import tuneuptechnology

client = tuneuptechnology.Client(os.getenv('API_EMAIL'), os.getenv('API_KEY'))

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
    },
)

print(customer)
