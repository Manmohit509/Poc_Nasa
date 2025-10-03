import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry
from enum import Enum

class DailyInfo(str, Enum):
    DATE = "date"
    RAIN_SUM = "rain_sum (mm)"
    HUMIDITY_2M_MEAN = "relative_humidity_2m_mean (%)"
    SURFACE_PRESSURE_MEAN = "surface_pressure_mean (hPa)"
    TEMPERATURE_2M_MEAN = "temperature_2m_mean (°C)"
    SHORTWAVE_RADIATION_SUM = "shortwave_radiation_sum (MJ/m²)"
    ET0_FAO_SUM = "et0_fao_evapotranspiration_sum (mm)"
    SUNSHINE_DURATION = "sunshine_duration (h)"
    WIND_SPEED_10M_MEAN = "wind_speed_10m_mean (m/s)"
    
# class weather_info:
    

def get_weather_info(lat:float, lon:float):
# Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    daily_var = [var.value for var in DailyInfo if var.value != "date"]
    params = {
    	"latitude": lat,
    	"longitude": lon,
        "daily": daily_var,
    	"utm_source": "Poc_Farmers",
    }
    responses = openmeteo.weather_api(url, params=params)
    
    response = responses[0]
    # Process daily data. The order of variables needs to be the same as requested.
    daily = response.Daily()
    daily_rain_sum = daily.Variables(0).ValuesAsNumpy()
    daily_relative_humidity_2m_mean = daily.Variables(1).ValuesAsNumpy()
    daily_surface_pressure_mean = daily.Variables(2).ValuesAsNumpy()
    daily_temperature_2m_mean = daily.Variables(3).ValuesAsNumpy()
    daily_shortwave_radiation_sum = daily.Variables(4).ValuesAsNumpy()
    daily_et0_fao_evapotranspiration_sum = daily.Variables(5).ValuesAsNumpy()
    daily_sunshine_duration = daily.Variables(6).ValuesAsNumpy()
    daily_wind_speed_10m_mean = daily.Variables(7).ValuesAsNumpy()

    daily_data = {"date": pd.date_range(
    	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
    	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
    	freq = pd.Timedelta(seconds = daily.Interval()),
    	inclusive = "left"
    )}

    daily_data["rain_sum (mm)"] = daily_rain_sum
    daily_data["relative_humidity_2m_mean (%)"] = daily_relative_humidity_2m_mean
    daily_data["surface_pressure_mean (hPa)"] = daily_surface_pressure_mean
    daily_data["temperature_2m_mean (°C)"] = daily_temperature_2m_mean
    daily_data["shortwave_radiation_sum (MJ/m²)"] = daily_shortwave_radiation_sum
    daily_data["et0_fao_evapotranspiration_sum (mm)"] = daily_et0_fao_evapotranspiration_sum
    daily_data["sunshine_duration (h)"] = daily_sunshine_duration
    daily_data["wind_speed_10m_mean (m/s)"] = daily_wind_speed_10m_mean
    
    daily_dataframe = pd.DataFrame(data = daily_data)
    daily_dataframe["date"] = daily_dataframe["date"].dt.strftime("%Y-%m-%d")
    return daily_dataframe
