import geopandas as gpd

gdf = gpd.read_file('EPSG900913.shp')
print(gdf['eq_enderec'].iloc[0])