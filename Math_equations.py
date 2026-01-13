import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("My First Map")

m = folium.Map(location=[30.45,-97.59], zoom_start=10)

folium.Marker(location=[30.632489,-97.735146], popup="River View", icon=folium.Icon(color="green", icon="cloud")).add_to(m)

st_folium(m, width=800, height=500)
























