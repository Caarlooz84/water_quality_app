import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Water Features")

#site = st.text_input("Enter site name")

site = st.selectbox("Choose a site:", ["River View", "Winding Creek", "Steele Creek", "Redbird", "Alamo Ranch", "Creekside"])

if site == "River View":
    m = folium.Map(location=[30.632489, -97.735146], zoom_start=12)
    folium.Marker(location=[30.632489, -97.735146], popup = "River View", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
    st_folium(m)

if site == "Winding Creek":
    m = folium.Map(location=[29.623099, -98.125060], zoom_start=12)
    folium.Marker(location=[29.623099, -98.125060], popup = "Winding Creek", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
    st_folium(m)

if site == "Steele Creek":
    m = folium.Map(location=[29.572180, -98.218894], zoom_start=12)
    folium.Marker(location=[29.572180, -98.218894], popup = "Steele Creek", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
    st_folium(m)

if site == "Redbird":
    m = folium.Map(location=[29.431115, -98.798014], zoom_start=12)
    folium.Marker(location=[29.431115, -98.798014], popup = "Redbird", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
    st_folium(m)

if site == "Alamo Ranch":
    m = folium.Map(location=[29.4834609, -98.7338868], zoom_start=12)
    folium.Marker(location=[29.4834609, -98.7338868], popup = "Alamo Ranch", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
    st_folium(m)

if site == "Creekside":
    m = folium.Map(location=[29.7298477, -98.0750534], zoom_start=12)
    folium.Marker(location=[29.7298477, -98.0750534], popup = "Creekside", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
    st_folium(m)

#If you want to post all in once:

# m = folium.Map(location=[###,###], zoom_start=#)

#folium.Marker([29.72, -98.1], popup="River View").add_to(m)
#folium.Marker([29.74, -98.15], popup="Lake Park").add_to(m)
#folium.Marker([29.70, -98.05], popup="Creek Side").add_to(m)
#etc.










