import streamlit as st
from streamlit_mic_recorder import mic_recorder, speech_to_text

state = st.session_state

if 'text_received' not in state:
    state.text_received = []

st.title("Search or speak your desired route:")

st.text_input(
    label= "Type your desired route 👇",
    placeholder="I want to go from Churubusco tu Coapa but i do not know how",
)

text = speech_to_text(
    language='es', use_container_width=True, just_once=True, key='STT')


if text:
    state.text_received.append(text)

for text in state.text_received:
    st.text(text)

def getText():
    return text


