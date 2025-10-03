import ee
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

PROJECT=os.getenv("PROJECT")
# Initialiser Earth Engine (nécessite une inscription gratuite)
# S'inscrire sur: https://earthengine.google.com/signup/
ee.Authenticate()
ee.Initialize(project=PROJECT)

def get_ndvi_statistics(lat, lon):

    days_back=7
    point = ee.Geometry.Point([lon, lat], proj='EPSG:4326')
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_back)
    
    collection = ee.ImageCollection('MODIS/061/MOD09GA') \
        .filterDate(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')) \
        .filterBounds(point)
    
    def calculate_ndvi(image):
        return image.normalizedDifference(['sur_refl_b02', 'sur_refl_b01']).rename('NDVI')
    
    ndvi_collection = collection.map(calculate_ndvi)
    
    # Réduire avec plusieurs statistiques
    stats = ndvi_collection.reduce(
        ee.Reducer.mean()
        .combine(ee.Reducer.min(), '', True)
        .combine(ee.Reducer.max(), '', True)
        .combine(ee.Reducer.stdDev(), '', True)
    )
    
    result = stats.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=point,
        scale=250,
        bestEffort=True
    ).getInfo()
    
    return (round(result.get('NDVI_max', 0), 3))

