from preprotools.available_taxi import AvailableTaxis

taxi = AvailableTaxis()

def test_url():
    assert taxi.url == 'https://api.data.gov.sg/v1/transport/taxi-availability'

def test_response():
    taxi.get_response()
    assert len(taxi.response) > 0
