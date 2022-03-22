import os

import tuneuptechnology

client = tuneuptechnology.Client(os.getenv('API_EMAIL'), os.getenv('API_KEY'))

inventory = client.Inventory.retrieve(id=23)

print(inventory)
