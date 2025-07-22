import csv
from dataclasses import dataclass
from datetime import datetime
from typing import List #find out if I need this

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

    def _extract_column_indices(self, header: list[str]) -> dict[str, int]:
        try:

            return {
                variable_name:header.index(csv_column_name)
                for (variable_name, csv_column_name) in self.REQUIRED_COLUMNS.items()
            }
            
        except ValueError as e:
            raise ValueError(f"Missing required column in CSV header: {e}")
    
    def clean_csv(self) -> List[CleanRow]:
        with open(self.filename) as csv_file:
            reader = csv.reader(csv_file)
            try:
                header = next(reader, None)
            except header is None:
                raise(ValueError("Header missing or csv file is empty."))
            

            indices = self._extract_column_indices(header)

            cleaned_data = []
            for row_number, row in enumerate(reader, start=2):
                try:
                    btc_price_string = row[indices["btc_close_price"]]
                    btc_price_float = float(btc_price_string)
                    date_string = row[indices["date"]]
                    date_datetime = datetime.strptime(date_string,"%Y-%m-%d").date()
                    cleaned_data.append(CleanRow(date = date_datetime, btc_close_price= btc_price_float))
                except (ValueError, IndexError) as e:
                    raise ValueError(f"Error parsing row {row_number}: {e}")
            return cleaned_data
                
    

x = DataCleaner("tests/test_return_list.csv").clean_csv()
print(x)