from dotenv import load_dotenv
from fredapi import Fred
import os

load_dotenv()

def get_fred_client():
    """
    Create and return an authenticated FRED client.
    """
    api_key = os.getenv("FRED_API_KEY")

    if api_key is None:
        raise ValueError("FRED_API_KEY not found")
    
    return Fred(api_key=api_key)

def get_series(series_id, start_date=None):
    """
    Download a FRED time series.
    """
    fred = get_fred_client()

    return fred.get_series(
        series_id,
        observation_start=start_date
    )