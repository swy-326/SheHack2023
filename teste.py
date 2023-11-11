import geopandas as gpd

gdf = gpd.read_file('EPSG900913.shp')
print(gdf['eq_enderec'].iloc[0])
import folium
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
gdf["latitude"]=lat
gdf["longitude"]=lon
