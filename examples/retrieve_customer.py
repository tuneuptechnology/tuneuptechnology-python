import os

import tuneuptechnology

client = tuneuptechnology.Client(os.getenv('API_EMAIL'), os.getenv('API_KEY'))

customer = client.Customers.retrieve(id=23)

print(customer.json())
