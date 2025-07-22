import csv
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class CleanRow:
    date: datetime
    btc_close_price: float

class DataCleaner:
    REQUIRED_COLUMNS = {
        "btc_close_price": "Close",
        "date": "End"
    }

    def __init__(self, filename):
        self.filename = filename

    def _extract_column_indices(self, header):
        return {index:column_name for (index,column_name) in enumerate(header) if column_name in self.REQUIRED_COLUMNS.values()}
    
    def clean_csv(self):
        with open(self.filename) as csv_file:
            reader = csv.reader(csv_file)
            try:
                header = next(reader, None)
            except header is None:
                raise(ValueError("Header missing or csv file is empty."))
            

            indices = self._extract_column_indices(header)
            print(indices)
    

x = DataCleaner("tests/test_return_list.csv").clean_csv()
