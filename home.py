import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome to SafeNav! 🚀")

st.header("Waze's Safety Upgrade")
st.write("Do you often feel unsafe when going home? Want to know the most optimal safe route to get there?.")

st.write("Then, SafeNav is the answer for you! Just easily type or speak your desired initial point and final destination point, and we will provide you with the safest route to get there.")

st.subheader("It is this easy to view your route on an interactive map with understandable instructions.")

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

st.divider()

st.page_link("pages\⭐ Get Started.py", label="Get Started", icon="🚀")

st.write("Thank you for choosing SafeNav!")
