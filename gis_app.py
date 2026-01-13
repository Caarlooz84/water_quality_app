# gis_app.py
import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium
from geodatasets import get_path

# Title shown in the Streamlit app
st.title("Step 1 — Simple GIS Map 🌎 ")

# Load GeoPandas' built-in 'world' dataset
world = gpd.read_file(get_path("nybb"))

# Show a quick preview of the GeoDataFrame
st.write("### Dataset preview")
st.write(world.head())

# Create a folium map centered near the middle of the world
m = folium.Map(location=[40.7, -73.9], zoom_start=10)

def style_function(feature):
    if feature['properties']['BoroName'] == 'Queens':
        return {'fillColor': 'pink', 'color': 'white', 'weight': 2, 'fillOpacity': 0.6}
    else:
        return {'fillColor': 'lightgray', 'color': 'black', 'weight': 1, 'fillOpacity': 0.4}

folium.GeoJson(
    world,
    name="All Boroughs",
    style_function=style_function,
    popup=folium.GeoJsonPopup(fields=["BoroName", "BoroCode"])  # <-- POPUP
).add_to(m)

# Add the GeoDataFrame as a GeoJSON layer on the folium map
#folium.GeoJson(world, name="world").add_to(m)

# Display the interactive folium map inside Streamlit
st.write("### Interactive map")
st_folium(m, width=800, height=500)