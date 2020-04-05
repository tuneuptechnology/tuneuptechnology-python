"""Create a customer record by passing in all required data"""
import os
from dotenv import load_dotenv
import tuneuptechnology

load_dotenv()
API_EMAIL = os.getenv('API_EMAIL')
API_KEY = os.getenv('API_KEY')

CUSTOMER = tuneuptechnology.Customers.create_customer(
    data={
        'auth': API_EMAIL,
        'api_key': API_KEY,
        'firstname': 'Jake',
		'lastname': 'Peralta',
		'email': 'jake@example.com',
		'phone': '8015551234',
		'user_id': 1,
		'notes': 'Believes he is a good detective.',
		'location_id': 1,
    }
)

tuneuptechnology.Util.pretty_print(CUSTOMER)
