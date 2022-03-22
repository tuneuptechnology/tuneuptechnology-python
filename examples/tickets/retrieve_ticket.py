import os

import tuneuptechnology

client = tuneuptechnology.Client(os.getenv('API_EMAIL'), os.getenv('API_KEY'))

ticket = client.Tickets.retrieve(id=23)

print(ticket)
