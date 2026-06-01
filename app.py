import streamlit as st

st.title("Hello App")

user_input = st.text_input("Your name")
st.write(f"Hello, {user_input}")