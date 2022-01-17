import vcr  # type: ignore

from tuneuptechnology.client import Client

custom_vcr = vcr.VCR(
    cassette_library_dir='test/cassettes/customers',
    path_transformer=vcr.VCR.ensure_suffix('.yml'),
    filter_headers=['Email', 'Api-Key'],
)


@custom_vcr.use_cassette()
def test_customer_create(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Customers.create(
        data={
            'firstname': 'Jake',
            'lastname': 'Peralta',
            'email': 'jake@example.com',
            'phone': '8015551234',
            'user_id': 1,
            'notes': 'Believes he is a good detective.',
            'location_id': 2,
        }
    )

    assert response['firstname'] == 'Jake'


@custom_vcr.use_cassette()
def test_customer_all(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Customers.all()

    assert len(response['data']) > 1


@custom_vcr.use_cassette()
def test_customer_retrieve(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Customers.retrieve(id=1)

    assert response['firstname']


@custom_vcr.use_cassette()
def test_customer_update(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Customers.update(
        id=1,
        data={
            'firstname': 'Jake',
            'lastname': 'Peralta',
            'email': 'jake@example.com',
            'phone': '8015551234',
            'user_id': 1,
            'notes': 'Believes he is a good detective.',
            'location_id': 2,
        },
    )

    assert response['firstname'] == 'Jake'


@custom_vcr.use_cassette()
def test_customer_delete(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Customers.delete(id=1)

    assert response['deleted_at']
