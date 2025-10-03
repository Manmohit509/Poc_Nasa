from get_weather_info import get_weather_info
from get_ndvi_statistics import get_ndvi_statistics

def get_all_extern_info(lat:float, lon:float):
    weather_info = get_weather_info(lat, lon).to_json(orient="records", date_format="iso")
    ndvi_info = get_ndvi_statistics(lat, lon)
    return {weather_info, ndvi_info}