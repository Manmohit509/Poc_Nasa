import math

def calculate_water_use(tmax: float, tmin: float, rain: float, rad: float, wind: float):
    # Conversion rayonnement net approximé
    rad *= 0.77 * 0.0864 # Rn ≈ 0.77 * (Rs * conversion) <-- MW/m² to MJ/m²

    # Constantes
    P = 101.3  # kPa, pression atmosphérique moyenne
    gamma = 0.000665 * P
    T_mean = (tmax + tmin) / 2

    # Pression de vapeur saturante (kPa)
    es = 0.6108 * math.exp((17.27 * T_mean) / (T_mean + 237.3))

    # Pression de vapeur réelle (approx. 50% si RH inconnue)
    ea = es * 0.5 #<-- chercher sur l api de open weather

    # Pente de la courbe de saturation
    delta = (4098 * es) / ((T_mean + 237.3) ** 2)

    # ET0 (mm/jour)
    ET0 = (0.408 * delta * rad + gamma * (900 / (T_mean + 273)) * wind * (es - ea)) / \
          (delta + gamma * (1 + 0.34 * wind))

    #todo faire le kc pour etre plus opti
    # Besoin net d’irrigation (mm/jour)
    water_need = max(ET0 - rain, 0) # verifier si c'est pas negatif d ou le besoin de pas arroser

    return water_need
