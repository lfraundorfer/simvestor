import csv
from dataclasses import dataclass
from datetime import datetime

# Receives a CSV file and returns a list of cleaned dates and closing prices for the downstream

@dataclass
class CleanRow:
    date: datetime
    close_price: float

class DataCleaner:
    REQUIRED_COLUMNS = {
        "close_price": "Close",
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
            
        except (ValueError, AttributeError) as e:
            raise ValueError(f"Missing required column in CSV header: {e}")
    
    def clean_csv(self) -> list[CleanRow]:
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
                    price_string = row[indices["close_price"]]
                    price_float = float(price_string)
                    date_string = row[indices["date"]]
                    date_datetime = datetime.strptime(date_string,"%Y-%m-%d").date()
                    cleaned_data.append(CleanRow(date = date_datetime, close_price= price_float))
                except (ValueError, IndexError) as e:
                    raise ValueError(f"Error parsing row {row_number}: {e}")
            return cleaned_data
                