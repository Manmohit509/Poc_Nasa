
def interpreter_ndvi(ndvi_value):
    """Interpréter la valeur NDVI"""
    if ndvi_value is None or ndvi_value < 0:
        return "Sol nu ou eau"
    elif 0 <= ndvi_value < 0.2:
        return "Sol nu - Végétation absente"
    elif 0.2 <= ndvi_value < 0.3:
        return "Végétation clairsemée - Santé faible ⚠️"
    elif 0.3 <= ndvi_value < 0.5:
        return "Végétation modérée - Santé moyenne ⚡"
    elif 0.5 <= ndvi_value < 0.7:
        return "Végétation dense - Bonne santé ✅"
    else:
        return "Végétation très dense - Excellente santé 🌟"
