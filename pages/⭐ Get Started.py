import streamlit as st

st.title("Welcome to My Streamlit App")

st.header("Introduction")
st.write("This is a simple Streamlit app to get you started.")

st.write("Here, you can add your content, such as text, images, charts, etc.")

user_input = st.text_input("Enter your name", "")

if user_input:
    st.write(f"Hello, {user_input}!")

st.image("assets/images/test.jpg", caption="Example Image", use_column_width=True)


st.write("Thank you for using my Streamlit app!")
