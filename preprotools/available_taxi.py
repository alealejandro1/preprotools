import pandas as pd
import requests
from datetime import datetime


class AvailableTaxis:
    """
    This class uses the API from LTA
    For access to real-time taxi availability data.
    Returns location coordinates of all
    Taxis that are currently available for hire.
    Does not include "Hired" or "Busy" Taxis.
    """

    def __init__(self):
        gov = 'https://api.data.gov.sg/v1'
        available_taxi_api_url = '/transport/taxi-availability'
        self.response = {}
        self.url = gov + available_taxi_api_url
        self.update_rate = 60 * 5
        self.row_df = pd.DataFrame([])
        self.csv_path = 'AvailableTaxi.csv'
        self.available_taxi_count = 0
        self.updated_taxi_df = pd.DataFrame([])

    def get_response(self):
        """
        Uses requests to update self.response
        """
        self.response = requests.get(self.url).json()

    def taxi_analytics(self):
        """
        Simple math based on the number of taxis
        """
        taxi_coordinates_df= pd.DataFrame.from_dict(self.response['features']
                                                    [0]['geometry']['coordinates'])
        taxi_coordinates_df=  taxi_coordinates_df.rename(columns = {0:'lon',1:'lat'})
        # self.available_taxi_count = taxi_coordinates_df.shape[0]
        self.available_taxi_count = -100
        self.updated_taxi_df = taxi_coordinates_df

    def get_available_taxi_count(self):
        print(f'At {datetime.now()} there are {self.available_taxi_count} taxis available')
