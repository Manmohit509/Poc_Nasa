
from service.water_info.water_info import water_info

from fastapi import FastAPI

app = FastAPI()

@app.get("/get-water-info")
def get_water_info(lat:float, lon:float):
    water_info(47.316667, 5.016667)