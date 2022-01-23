import time
from BaseExtractor import BaseExtractor
import pandas as pd
import itertools
import json
import schedule
from schedule import every, repeat
from datetime import datetime

URL = 'https://www.iaa.gov.il/en/airports/ben-gurion/flight-board/'


class FlightExtractor(BaseExtractor):

    def __init__(self):
        super().__init__()

    @repeat(every(1).minutes)
    def get_data(self):
        self.get(URL)
        # Get the table headers
        table_headers = self.get_any_elements_by_xpath("//table[@id='flight_board-arrivel_table']//thead//tr//th")
        # Put headers names into a list
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
        now = datetime.now()
        dt_string = now.strftime("%m-%d-%y_%H-%M-%S")
        with open(f'C:/Users/Gil/PycharmProjects/Matrix_Selenium/ft{dt_string}.json', "w+") as file:
            json.dump(flights_json, file)
        self.refresh()

    def search(self, expression, file_type='.json'):
        self.search(expression, file_type)


def main():
    flight = FlightExtractor()
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
