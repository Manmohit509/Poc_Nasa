import requests

def get_city_coordinates(city):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "city": city,
        "format": "json"
    }
    headers = {
        # Put something that identifies your project or email
        "User-Agent": "MyGeocoderApp/1.0 (contact@example.com)",
        "Accept": "application/json"
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()

    if not data:
        raise ValueError(f"City '{city}' not found")

    lat = data[0]["lat"]
    lon = data[0]["lon"]

    return {"city": city, "lat": lat, "lon": lon}

