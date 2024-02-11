import streamlit as st
import os
from streamlit_mic_recorder import speech_to_text
import gspread
from google.oauth2.service_account import Credentials

creds = {
    'type': os.environ['type'],
    'project_id': os.environ['project_id'],
    'private_key_id': os.environ['private_key_id'],
    'private_key': os.environ['private_key'],
    'client_email': os.environ['client_email'],
    'client_id': os.environ['client_id'],
    'auth_uri': os.environ['auth_uri'],
    'token_uri': os.environ['token_uri'],
    'auth_provider_x509_cert_url': os.environ['auth_provider_x509_cert_url'],
    'client_x509_cert_url': os.environ['client_x509_cert_url']
}

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = Credentials.from_service_account_file(creds, scopes=scope)

client = gspread.authorize(creds)

sheet = client.open('Streamlit SafeNav').worksheet('Hoja 1')

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

# Reminder to always read cell A1, which is where the last text is stored
for text in state.text_received:
    container.text(text)
    print(text + " < - Saved to file")
    with open('text.txt', 'w') as f:
        f.write(text)
        row = [[text]]
        sheet.insert_cols(row, 1)

st.button("Search Route", use_container_width=True)

st.divider()


#st.page_link("pages/🕷️ Report a bug.py", label="Click this button to Report a bug", icon="🕷️")

st.divider()

st.write("Thank you for choosing SafeNav!")




