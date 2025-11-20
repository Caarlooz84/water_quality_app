import os
print("Current working directory:", os.getcwd())
import geopandas as gpd
import matplotlib.pyplot as plt
land = gpd.read_file("ne_10m_land.shp")
print("First 5 rows of the land data:")
print(land.head())
land.plot()
plt.title("Land Polygons")
plt.show()