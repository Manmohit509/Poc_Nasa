from Backend.service.get_health import interpreter_ndvi
from service.get_all_extern_info.get_all_externe_info import get_all_extern_info

from fastapi import FastAPI

app = FastAPI()

@app.get("/get-all-extern-info")
def all_extern_info(lat:float, lon:float):
    return get_all_extern_info(lat, lon)


@app.get("/get-health-interpretation")
def health_interpretation(ndvi: float):
    return interpreter_ndvi(ndvi_value=ndvi)
