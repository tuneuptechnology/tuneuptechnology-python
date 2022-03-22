import os

import tuneuptechnology

client = tuneuptechnology.Client(os.getenv('API_EMAIL'), os.getenv('API_KEY'))

location = client.Locations.retrieve(id=23)

print(location)
