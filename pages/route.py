import streamlit as st
from streamlit_mic_recorder import speech_to_text
from api.gsheet_auth import gsheet_auth
from api.filtering_gpt import ask_gpt
from algorithms.pathClass import pathfinder

searchRoute = pathfinder()
client = gsheet_auth()
sheet = client.open('Streamlit SafeNav').worksheet('Hoja 1')

state = st.session_state

if 'text_received' not in state:
    state.text_received = []

st.title("Search or speak your desired route 🗺️")

st.divider()
st.write("Remember to only search or ask for entities in Mexico City, such as: ")
st.write("Churubusco, Coapa, Tacuba, Moctezuma, La Noria, Dinamo, etc.")

typed_route = st.text_input(
    label= "Type your desired route 👇",
    placeholder="I want to go from Churubusco tu Coapa but i do not know how",
)

text = speech_to_text(
    language='es', use_container_width=True, just_once=True, key='STT')

container = st.container(border=True)

if text:
    state.text_received.append(text)
    container.text(text)

            
if st.button("Search Route", use_container_width=True):
    if typed_route:
        st.info("Calculating the safest route... 🚗🔍")
        response = ask_gpt(typed_route)
        routeFound = searchRoute.gptDecoder(response)
        st.write(routeFound)
        sheet.append_row([typed_route, response])  
    else:
        st.info("Calculating the safest route... 🚗🔍")
        prompt = state.text_received[-1]
        response = ask_gpt(prompt)
        routeFound = searchRoute.gptDecoder(response)
        st.write(routeFound)
        sheet.append_row([prompt, response])
    
st.divider()

st.page_link("pages/🕷️ Report a bug.py", label="Click this button to Report a bug", icon="🕷️")

st.divider()

st.write("Thank you for choosing SafeNav!")






