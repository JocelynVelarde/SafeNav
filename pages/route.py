import streamlit as st
from streamlit_mic_recorder import speech_to_text

state = st.session_state

if 'text_received' not in state:
    state.text_received = []

st.title("Search or speak your desired route 🗺️")

st.divider()

st.text_input(
    label= "Type your desired route 👇",
    placeholder="I want to go from Churubusco tu Coapa but i do not know how",
)

text = speech_to_text(
    language='es', use_container_width=True, just_once=True, key='STT')

if text:
    state.text_received.append(text)

container = st.container(border=True)
for text in state.text_received:
    container.text(text)
    print(text + " < - Saved to file")
    with open('text.txt', 'w') as f:
        f.write(text)

st.button("Search Route", use_container_width=True)

st.divider()


#st.page_link("pages/🕷️ Report a bug.py", label="Click this button to Report a bug", icon="🕷️")

st.divider()

st.write("Thank you for choosing SafeNav!")




