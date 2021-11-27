import pandas as pd
import requests

class Temperature:
    """
    This class was made to retrieve data from the API for Weather in Singapore.
    Data is updated every 5 minutes.
    """
    def __init__(self):
        self.response = {}
        self.url = 'https://api.data.gov.sg/v1'+'/environment/air-temperature'
        self.update_rate = 60 * 5
        self.row_df = pd.DataFrame([])
        self.csv_path = 'Temperature.csv'

    def get_response(self):
        """
        Uses requests to update self.response
        """
        self.response = requests.get(self.url).json()

    def make_row(self):
        """
        Takes a JSON response from the API and parses it into a dataframe row.
        This is to be appended outside
        """
        temp_dic = {}
        n_stations = len(self.response['items'][0]['readings'])
        for station in range(n_stations):
            temp_dic[self.response['items'][0]['readings'][station
                                            ]['station_id']]=self.response['items'][0]['readings'][station]['value']
        temp_df = pd.DataFrame.from_dict(temp_dic, orient='index').T
        temp_df['timestamp']=self.response['items'][0]['timestamp']
        self.row_df = temp_df

    def write_csv(self):
        with open(self.csv_path, 'a') as file:
            self.row_df.to_csv(file, mode='a', index=False,  header=file.tell()==0)
        return
