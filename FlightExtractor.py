import time
from BaseExtractor import BaseExtractor
import pandas as pd
import itertools
import json
import schedule
from schedule import every, repeat
from datetime import datetime
import os

URL = 'https://www.iaa.gov.il/en/airports/ben-gurion/flight-board/'


class FlightExtractor(BaseExtractor):

    def __init__(self):
        super().__init__()

    def store_data(self, saved_file):
        directory = 'saved_flights'
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, directory)
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        print(path)
        now = datetime.now()
        dt_string = now.strftime("%m-%d-%y_%H-%M-%S")
        with open(f'{path}/ft{dt_string}.json', "w+") as file:
            json.dump(saved_file, file)

    def get_data(self):
        self.get(URL)
        # Get the table headers
        # Put headers names into a list
        table_headers = self.get_any_elements_by_xpath("//table[@id='flight_board-arrivel_table']//thead//tr//th")
        columns = list(map(lambda name: name.text, table_headers))
        # Click on show more until button is gone
        while True:
            try:
                self.get_clickable("//button[@id='next']")
            except:
                break
        # Get the table rows
        table = self.get_table("//*[@id='flight_board-arrivel_table']")
        # Put the rows into a list
        list_to_break = [cell.text for row in table.find_elements_by_css_selector('tr') for cell in
                         row.find_elements_by_tag_name('td')]
        # Break the list into a nested list - each list is a row
        result = [list(v) for k, v in itertools.groupby(list_to_break, key=lambda sep: sep == "") if not k]
        # Insert into Pandas Dataframe.
        df_flights = pd.DataFrame(result, columns=columns)
        # Convert table to json.
        flights_json = df_flights.to_json(orient='table', indent=4)
        # Storing the data extracted
        self.store_data(flights_json)


if __name__ == '__main__':
    flight = FlightExtractor()
    '''schedule.every(1).minutes.do(flight.get_data)

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            break'''
    flight.search(expression='Expression', filetype='.json', flag="flights")
    flight.shutdown()
