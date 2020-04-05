"""Retrieve all customers"""
import os
from dotenv import load_dotenv
import tuneuptechnology

load_dotenv()
API_EMAIL = os.getenv('API_EMAIL')
API_KEY = os.getenv('API_KEY')

CUSTOMERS = tuneuptechnology.Customers.retrieve_customers(
    data={
        'auth': API_EMAIL,
        'api_key': API_KEY,
    }
)

tuneuptechnology.Util.pretty_print(CUSTOMERS)
