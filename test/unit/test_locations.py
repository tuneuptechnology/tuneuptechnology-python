import vcr  # type: ignore

from tuneuptechnology.client import Client

custom_vcr = vcr.VCR(
    cassette_library_dir='test/cassettes/locations',
    path_transformer=vcr.VCR.ensure_suffix('.yml'),
    filter_headers=['Email', 'Api-Key'],
)


@custom_vcr.use_cassette()
def test_location_create(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Locations.create(
        data={
            'name': 'Location Name',
            'street': '123 California Ave',
            'city': 'Salt Lake',
            'state': 'UT',
            'zip': 84043,
        }
    )

    assert response['name'] == 'Location Name'


@custom_vcr.use_cassette()
def test_location_all(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Locations.all()

    assert len(response['data']) > 1


@custom_vcr.use_cassette()
def test_location_retrieve(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Locations.retrieve(id=1)

    assert response['name']


@custom_vcr.use_cassette()
def test_location_update(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Locations.update(
        id=1,
        data={
            'name': 'Location Name',
            'street': '123 California Ave',
            'city': 'Salt Lake',
            'state': 'UT',
            'zip': 84043,
        },
    )

    assert response['name'] == 'Location Name'


@custom_vcr.use_cassette()
def test_location_delete(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Locations.delete(id=1)

    assert response['deleted_at']
