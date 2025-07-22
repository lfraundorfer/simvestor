import pytest
import datetime
from datacleaner import DataCleaner


def test_read_file_and_return_list():
    cleanData = DataCleaner('tests/test_csv_files/test_return_list.csv').clean_csv()
    assert isinstance(cleanData, list)
    assert len(cleanData) > 0

def test_extract_column_indices():
    cleaner = DataCleaner('tests/test_csv_files/test_return_list.csv')
    indices = cleaner._extract_column_indices(["End", "Close"])
    assert indices["date"] == 0
    assert indices["btc_close_price"] == 1

def test_output_has_float_and_date():
    cleanData = DataCleaner('tests/test_csv_files/test_return_list.csv').clean_csv()
    for clean_data_entry in cleanData:
        assert isinstance(clean_data_entry.btc_close_price, float) and isinstance(clean_data_entry.date, datetime.date)

def test_fail_on_missing_file_headers():
    with pytest.raises(ValueError):
        cleanData = DataCleaner('tests/test_csv_files/test_header_missing.csv').clean_csv()

def test_fail_on_empty_file():
    with pytest.raises(ValueError):
        cleanData = DataCleaner('tests/test_csv_files/test_empty_file.csv').clean_csv()

def test_fail_on_missing_price():
    with pytest.raises(ValueError):
        cleanData = DataCleaner('tests/test_csv_files/test_missing_price.csv').clean_csv()

def test_fail_on_missing_date():
    with pytest.raises(ValueError):
        cleanData = DataCleaner('tests/test_csv_files/test_missing_date.csv').clean_csv()

def test_fail_on_nonnumeric_price():
    with pytest.raises(ValueError):
        cleanData = DataCleaner('tests/test_csv_files/test_nonnumeric_price.csv').clean_csv()
    

def test_fail_on_nonnumeric_date():
    with pytest.raises(ValueError):
        cleanData = DataCleaner('tests/test_csv_files/test_nonnumeric_date.csv').clean_csv()
    

def test_fail_on_invalid_date_format():
    with pytest.raises(ValueError):
        cleanData = DataCleaner('tests/test_csv_files/test_invalid_date_format.csv').clean_csv()
    