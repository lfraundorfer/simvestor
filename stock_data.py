from datacleaner import CleanRow

def match_dates(sp_data:CleanRow, btc_data:CleanRow):
    shared_dates = set(item.date for item in sp_data) & set(item.date for item in btc_data)
    filtered_sp500 = [row for row in sp_data if row.date in shared_dates]
    filtered_btc = [row for row in btc_data if row.date in shared_dates]
    filtered_sp500 = sorted(filtered_sp500, key=lambda x: x.date)
    filtered_btc = sorted(filtered_btc, key=lambda x: x.date)
    return filtered_btc, filtered_sp500


# clean_data_sp = DataCleaner("data/sp500_historical_data.csv").clean_csv()
# clean_data_btc = DataCleaner("data/btc_historical_data.csv").clean_csv()

# match_dates(clean_data_sp, clean_data_btc)


