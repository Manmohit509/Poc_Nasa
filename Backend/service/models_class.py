from pydantic import BaseModel, Field
from enum import Enum
from typing import List

class GrowthStage(Enum):
    INITIAL = "initial"
    MID = "mid"
    FINAL = "final"

class WeatherDay(BaseModel):
    date: str
    rain_sum_mm: float = Field(..., alias="rain_sum (mm)")
    relative_humidity_2m_mean_pct: float = Field(..., alias="relative_humidity_2m_mean (%)")
    surface_pressure_mean_hpa: float = Field(..., alias="surface_pressure_mean (hPa)")
    temperature_2m_mean_c: float = Field(..., alias="temperature_2m_mean (°C)")
    shortwave_radiation_sum_mj_m2: float = Field(..., alias="shortwave_radiation_sum (MJ/m²)")
    et0_fao_evapotranspiration_sum_mm: float = Field(..., alias="et0_fao_evapotranspiration_sum (mm)")
    sunshine_duration_h: float = Field(..., alias="sunshine_duration (h)")
    wind_speed_10m_mean_ms: float = Field(..., alias="wind_speed_10m_mean (m/s)")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True

class CutureGeneralInfo(BaseModel):
    ndvi: float
    culture: str
    stade_of_culture: GrowthStage

class WaterRequest(BaseModel):
    weather_info: List[WeatherDay]
    cutureGeneralInfo : CutureGeneralInfo
