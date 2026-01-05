import requests
import json
import pandas as pd

BLS_API_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

def fetch_bls_series(series_id, start_year, end_year):
    payload = {
        "seriesid": [series_id],
        "startyear": start_year,
        "endyear": end_year
    }

    response = requests.post(
        BLS_API_URL,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )

    response.raise_for_status()
    data = response.json()["Results"]["series"][0]["data"]
    return pd.DataFrame(data)

