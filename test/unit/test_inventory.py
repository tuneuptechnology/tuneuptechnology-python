import vcr  # type: ignore

from tuneuptechnology.client import Client

custom_vcr = vcr.VCR(
    cassette_library_dir='test/cassettes/inventory',
    path_transformer=vcr.VCR.ensure_suffix('.yml'),
    filter_headers=['Email', 'Api-Key'],
)


@custom_vcr.use_cassette()
def test_inventory_create(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Inventory.create(
        data={
            'name': 'Inventory Item',
            'inventory_type_id': 1,
            'part_number': '1234',
            'sku': '1234',
            'notes': 'here are some notes',
            'part_price': '19.99',
            'location_id': 2,
            'quantity': 1,
        }
    )

    assert response['name'] == 'Inventory Item'


@custom_vcr.use_cassette()
def test_inventory_all(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Inventory.all()

    assert len(response['data']) > 1


@custom_vcr.use_cassette()
def test_inventory_retrieve(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Inventory.retrieve(id=1)

    assert response['name']


@custom_vcr.use_cassette()
def test_inventory_update(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Inventory.update(
        id=1,
        data={
            'name': 'Inventory Item',
            'inventory_type_id': 1,
            'part_number': '1234',
            'sku': '1234',
            'notes': 'here are some notes',
            'part_price': '19.99',
            'location_id': 2,
            'quantity': 1,
        },
    )

    assert response['name'] == 'Inventory Item'


@custom_vcr.use_cassette()
def test_inventory_delete(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Inventory.delete(id=1)

    assert response['deleted_at']
