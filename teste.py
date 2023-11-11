import geopandas as gpd

import folium
gdf = gpd.read_file('EPSG900913.shp')

lat=[]
lon=[]
from geopy.geocoders import Nominatim

for i in range(len(gdf)):
    end=gdf['eq_enderec'].iloc[i]
    # Obter as coordenadas a partir do endereço
    geolocator = Nominatim(user_agent="my_app")
    try:
        location = geolocator.geocode(end)
        lat.append(location.latitude)
        lon.append(location.longitude)
    except:
        lat.append("")
        lon.append("")

data = {'latitude': lat, 'longitude': lon,}
