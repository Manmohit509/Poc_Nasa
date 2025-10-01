from service.water_info.get_wheather_info import get_weather_info
from service.water_info.calculate_water_use import calculate_water_use


def water_info(lat: float, long: float):
    prevision = []
    data_info = []
    wheater_data = get_weather_info(lat, long)
    for i, day in enumerate(wheater_data["time"]):
        tmax  = float(wheater_data["temperature_2m_max"][i])
        tmin = float(wheater_data["temperature_2m_min"][i])
        rain = float(wheater_data["precipitation_sum"][i])
        rad = float(wheater_data["shortwave_radiation_sum"][i])
        wind = float(wheater_data["wind_speed_10m_max"][i])

        day_prevision = calculate_water_use(tmax,tmin,rain,rad,wind)
        data_info.append({"date" : day, "Temperature_mean (°C)" : (tmax + tmin) / 2, "rain (mm)" : rain, "wind (m/s)" : wind})
        prevision.append({"date": day, "water-use" : day_prevision})
    return {"info" : data_info, "prevision": prevision}
