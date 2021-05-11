import vcr
from tuneuptechnology.client import Client

ID = 1


@vcr.use_cassette('test/cassettes/locations/test_location_create.yml', filter_headers=['Email', 'Api-Key'])
def test_location_create(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Locations.create(
        data={
            'name': 'Location Name',
            'street': '123 California Ave',
            'city': 'Salt Lake',
            'state': 'UT',
            'zip': 84043
        }
    )

    assert response.status_code == 200


@vcr.use_cassette('test/cassettes/locations/test_location_all.yml', filter_headers=['Email', 'Api-Key'])
def test_location_all(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Locations.all()

    assert response.status_code == 200


@vcr.use_cassette('test/cassettes/locations/test_location_retrieve.yml', filter_headers=['Email', 'Api-Key'])
def test_location_retrieve(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Locations.retrieve(id=ID)

    assert response.status_code == 200


@vcr.use_cassette('test/cassettes/locations/test_location_update.yml', filter_headers=['Email', 'Api-Key'])
def test_location_update(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Locations.update(
        id=ID,
        data={
            'name': 'Location Name',
            'street': '123 California Ave',
            'city': 'Salt Lake',
            'state': 'UT',
            'zip': 84043
        }
    )

    assert response.status_code == 200


@vcr.use_cassette('test/cassettes/locations/test_location_delete.yml', filter_headers=['Email', 'Api-Key'])
def test_location_delete(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Locations.delete(id=ID)

    assert response.status_code == 200
