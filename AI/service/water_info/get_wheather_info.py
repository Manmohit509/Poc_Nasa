import requests
import os
from datetime import date
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()
api_key = os.environ.get('API_KEY')

def get_weather_info(lat:float, long:float):

    VARIABLES = ",".join([
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "wind_speed_10m_max",
        "shortwave_radiation_sum",
        "sunshine_duration"
    ])

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={long}"
        f"&daily={VARIABLES}"
        f"&forecast_days=7&timezone=auto"
    )

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()["daily"]
    if not data:
            raise ValueError(f"City (lat, lon):'{lat, long}' not found")
    return data
