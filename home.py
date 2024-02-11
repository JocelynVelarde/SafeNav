import streamlit as st
import pandas as pd
import numpy as np
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()
st.title("Welcome to SafeNav! 🚀")

st.divider()

for row in df:
    st.write(row)

st.header("🛡️Waze's Safety Upgrade🛡️")
st.write("Do you often feel unsafe when going home? Want to know the most optimal safe route to get there?.")

st.write("Then, SafeNav is the answer for you! Just easily type or speak your desired initial point and final destination point, and we will provide you with the safest route to get there.")

st.subheader(":blue[It is this easy to view your route on an interactive map with understandable instructions.]")

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

container = st.container(border=True)
container.map(df)

st.divider()

#st.page_link("pages\get_started.py", label="Click this button to Get Started", icon="🚀")

st.divider()

st.write("Thank you for choosing SafeNav!")
