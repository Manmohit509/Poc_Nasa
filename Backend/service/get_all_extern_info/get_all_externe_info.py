from .get_weather_info import get_weather_info

from .get_ndvi_statistics import get_ndvi_statistics

def get_all_extern_info(lat:float, lon:float):
    weather_info_df = get_weather_info(lat, lon)
    weather_info_json = weather_info_df.to_dict(orient="records")
    ndvi_info = get_ndvi_statistics(lat, lon)
    return { "weather_info": weather_info_json, "ndvi": ndvi_info}