

import csv

from service.models_class import CutureGeneralInfo, WaterRequest

kc_dict = {}

with open('kc_data.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        kc_dict[row['Culture']] = {
            'initial': float(row['Kc Initial']),
            'mid': float(row['Kc Moyen']),
            'final': float(row['Kc Final'])
        }

def calculate_water_use(et0: float, rain: float, kc:float):
    ETc = et0 * kc
    water_need = max(ETc - rain, 0)

    return water_need

def analyse_water_need(Info: WaterRequest):
    culture : CutureGeneralInfo = Info.cutureGeneralInfo
    kc = kc_dict[culture.culture][culture.stade_of_culture.value]
    water_need = []
    for day in Info.weather_info:
        water_need.append({"date" : day.date, "need" : calculate_water_use(kc=kc, rain=day.rain_sum_mm, et0=day.et0_fao_evapotranspiration_sum_mm)})
    return water_need