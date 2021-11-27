from preprotools.available_taxi import AvailableTaxis

taxi = AvailableTaxis()

def test_url():
    assert taxi.url == 'https://api.data.gov.sg/v1/transport/taxi-availability'

def test_response():
    taxi.get_response()
    assert len(taxi.response) > 0

def test_amount_taxis():
    taxi.get_response()
    taxi.taxi_analytics()
    assert taxi.available_taxi_count > 0
    assert taxi.available_taxi_count < 10000
