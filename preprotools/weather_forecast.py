import pandas as pd
import requests

class WeatherForecast():
    """
    This class implements the API from NEA
    Updated half-hourly from NEA
    2 Hour Weather Forecast
    The area_metadata field in the response provides
    longitude/latitude information for the areas.
    You can use that to place the forecasts on a map.
    """

    def __init__(self):
        gov = 'https://api.data.gov.sg/v1'
        forecast_url = '/environment/2-hour-weather-forecast'
        self.response = {}
        self.url = gov + forecast_url
        self.update_rate = 60 * 30
        self.row_df = pd.DataFrame([])
        self.csv_path = 'WeatherForecast.csv'
        self.updated_df = pd.DataFrame([])
        self.location_gps = pd.DataFrame([])

    def get_response(self):
        """
        Uses requests to update self.response
        """
        self.response = requests.get(self.url).json()
