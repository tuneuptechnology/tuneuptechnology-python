import os

import tuneuptechnology

API_EMAIL = os.getenv('API_EMAIL')
API_KEY = os.getenv('API_KEY')

client = tuneuptechnology.Client(API_EMAIL, API_KEY)

customer = client.Customers.retrieve(id=23)

print(customer.json())
