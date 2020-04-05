"""Retrieve a single customer record"""
import os
from dotenv import load_dotenv
import tuneuptechnology

load_dotenv()
API_EMAIL = os.getenv('API_EMAIL')
API_KEY = os.getenv('API_KEY')

CUSTOMER = tuneuptechnology.Customers.retrieve_customer(
    data={
        'auth': API_EMAIL,
        'api_key': API_KEY,
		'id': 23 # the ID of the customer you are retrieving
    }
)

tuneuptechnology.Util.pretty_print(CUSTOMER)
