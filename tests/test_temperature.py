from preprotools.temperature import Temperature

temp = Temperature()

def test_url():
    assert temp.url == 'https://api.data.gov.sg/v1/environment/air-temperature'

def test_response():
    temp.get_response()
    assert len(temp.response) > 0
