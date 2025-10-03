from service.models_class import GrowthStage
from .get_weather_info import get_weather_info

from .get_ndvi_statistics import get_ndvi_statistics

def get_all_extern_info(lat:float, lon:float,culture: str, stade_of_culture: GrowthStage):
    weather_info_df = get_weather_info(lat, lon)
    weather_info_json = weather_info_df.to_dict(orient="records")
    ndvi_info = get_ndvi_statistics(lat, lon)
    return { "weather_info": weather_info_json, "cutureGeneralInfo" : {"ndvi": ndvi_info, "culture": culture,"stade_of_culture": stade_of_culture}}