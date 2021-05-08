import vcr
from tuneuptechnology.client import Client

ID = 1


@vcr.use_cassette('test/fixtures/cassettes/customers/test_customer_create.yml', filter_headers=['Email', 'Api-Key'])
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

    assert response.status_code == 200


@vcr.use_cassette('test/fixtures/cassettes/customers/test_customer_all.yml', filter_headers=['Email', 'Api-Key'])
def test_customer_all(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Customers.all()

    assert response.status_code == 200


@vcr.use_cassette('test/fixtures/cassettes/customers/test_customer_retrieve.yml', filter_headers=['Email', 'Api-Key'])
def test_customer_retrieve(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Customers.retrieve(id=ID)

    assert response.status_code == 200


@vcr.use_cassette('test/fixtures/cassettes/customers/test_customer_update.yml', filter_headers=['Email', 'Api-Key'])
def test_customer_update(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Customers.update(
        id=ID,
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

    assert response.status_code == 200


@vcr.use_cassette('test/fixtures/cassettes/customers/test_customer_delete.yml', filter_headers=['Email', 'Api-Key'])
def test_customer_delete(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Customers.delete(id=ID)

    assert response.status_code == 200
