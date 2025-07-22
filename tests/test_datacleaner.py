import pytest
from datacleaner import DataCleaner




def test_read_file_and_return_list():
    cleanData = DataCleaner('tests/test_return_list.csv').clean_csv()
    assert isinstance(cleanData, list)

    
    
    # with open('tests/btc_test_data.csv') as csvfile:
    #     reader = csv.reader(csvfile, delimiter = ",")



# def test_find_missing_price():
#     with open('btc_test_data.csv') as csvfile:
#         reader = csv.reader(csvfile, delimiter = ",")


# def test_find_missing_date():
#     with open('btc_test_data.csv') as csvfile:
#         reader = csv.reader(csvfile, delimiter = ",")