from datetime import date

def list_years(dates: list):
    asc_dates = sorted(dates)
    for i, d in enumerate(asc_dates):
        asc_dates[i] = d.year
    return asc_dates