import os

import tuneuptechnology

API_EMAIL = os.getenv('API_EMAIL')
API_KEY = os.getenv('API_KEY')

client = tuneuptechnology.Client(API_EMAIL, API_KEY)

customers = client.Customers.all()

print(customers.json())
