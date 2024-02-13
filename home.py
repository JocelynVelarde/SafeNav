import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome to SafeNav! 🚀")
st.divider()

st.header("🛡️Waze's Safety Upgrade🛡️")
st.write("Do you often feel unsafe when going home? Want to know the most optimal safe route to get there?.")

st.write("Then, SafeNav is the answer for you! Just easily type or speak your desired initial point and final destination point, and we will provide you with the safest route to get there.")

st.subheader(":blue[It is this easy to view your route on an interactive map with understandable instructions.]")
"""
df_map = pd.read_csv("assets/files/polygons.csv")
df_map['geometry'] = df_map['geometry'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(df_map, crs='epsg:6362')
container = st.container(border=True)

container.map(gdf)



#failed iterations of maps
gdf = gpd.read_file('assets/files/polygons.csv')

container = st.container(border=True)

container.map(gdf)
#default
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

container = st.container(border=True)
container.map(df)
"""
mexico_city_coords = [19.4326, -99.1332]

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + mexico_city_coords,
    columns=['lat', 'lon'])


container = st.container(border=True)
container.map(df)
st.divider()

st.page_link("pages/get_started.py", label="Click this button to Get Started", icon="🚀")

st.divider()

st.write("Thank you for choosing SafeNav!")
