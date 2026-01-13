# gis_app.py
import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Title shown in the Streamlit app
st.title("Step 1 — Simple GIS Map")

# Load GeoPandas' built-in 'world' dataset
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Show a quick preview of the GeoDataFrame
st.write("### Dataset preview")
st.write(world.head())

# Create a folium map centered near the middle of the world
m = folium.Map(location=[20, 0], zoom_start=2)

# Add the GeoDataFrame as a GeoJSON layer on the folium map
folium.GeoJson(world, name="world").add_to(m)

# Display the interactive folium map inside Streamlit
st.write("### Interactive map")
st_folium(m, width=800, height=500)