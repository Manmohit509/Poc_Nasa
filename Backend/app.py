from typing import List
from service.models_class import GrowthStage, WaterRequest
from service.analyze_tool.analyse_water_need import analyse_water_need
from service.get_health import interpreter_ndvi
from service.get_all_extern_info.get_all_externe_info import get_all_extern_info

from fastapi import FastAPI

app = FastAPI()

@app.get("/extern-info")
def get_extern_info(lat: float, lon: float, culture: str, stade_of_culture: GrowthStage):
    return get_all_extern_info(lat, lon, culture, stade_of_culture)

@app.get("/health-interpretation")
def get_health_interpretation(ndvi: float):
    return interpreter_ndvi(ndvi_value=ndvi)

@app.post("/analyse-water-need")
def get_analyse_water_need(waterRequest: WaterRequest):
    return analyse_water_need(waterRequest)