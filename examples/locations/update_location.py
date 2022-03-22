import os

import tuneuptechnology

client = tuneuptechnology.Client(os.getenv('API_EMAIL'), os.getenv('API_KEY'))

location = client.Locations.update(
    id=23,
    data={
        'name': 'Location Name',
        'street': '123 California Ave',
        'city': 'Salt Lake',
        'state': 'UT',
        'zip': 84043,
    },
)

print(location)
