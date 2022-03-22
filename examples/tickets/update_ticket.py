import os

import tuneuptechnology

client = tuneuptechnology.Client(os.getenv('API_EMAIL'), os.getenv('API_KEY'))

ticket = client.Tickets.update(
    id=23,
    data={
        'customer_id': 1,
        'ticket_type_id': 1,
        'serial': '10000',
        'user_id': 1,
        'notes': 'here are some notes',
        'title': 'Fancy Title',
        'status': 1,
        'device': '2',
        'imei': 10000,
        'location_id': 1,
    },
)

print(ticket)