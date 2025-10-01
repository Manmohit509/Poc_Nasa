
from AI.service.water_info import water_info
from fastapi import FastAPI

app = FastAPI()

@app.get("/get-water-info")
def get_water_info(lat:float, lon:float):
    water_info(lat, lon)