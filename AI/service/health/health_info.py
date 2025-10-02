import requests
from shapely.geometry import Point, shape

def get_glam_id_from_latlon(lat, lon):
    """
    Retourne l'ID GLAM correspondant à une coordonnée GPS.
    
    Args:
        lat (float): latitude
        lon (float): longitude
        
    Returns:
        int: ID GLAM de la région contenant le point
    """
    # Récupère toutes les régions disponibles
    url = "https://glam1.gsfc.nasa.gov/api/regionlist/v1"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Erreur {response.status_code} : {response.text}")
    
    regions = response.json()
    point = Point(lon, lat)
    
    # Parcours des régions pour trouver celle qui contient le point
    for region in regions:
        if 'geometry' in region:
            geom = shape(region['geometry'])
            if geom.contains(point):
                return region['id']
    
    raise ValueError("Aucune région GLAM ne contient ce point.")

# Exemple d'utilisation
lat, lon = 48.8566, 2.3522  # Paris
glam_id = get_glam_id_from_latlon(lat, lon)
print("ID GLAM correspondant :", glam_id)
