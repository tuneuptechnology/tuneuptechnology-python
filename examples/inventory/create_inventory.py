import os

import tuneuptechnology

client = tuneuptechnology.Client(os.getenv('API_EMAIL'), os.getenv('API_KEY'))

inventory = client.Inventory.create(
    {
        'name': 'Inventory Item',
        'inventory_type_id': 1,
        'part_number': '1234',
        'sku': '1234',
        'notes': 'here are some notes',
        'part_price': 19.99,
        'location_id': 1,
        'quantity': 1,
    }
)

print(inventory)
