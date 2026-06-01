import streamlit as st # to create a web app
from datetime import date # to get todays date

st.title("Hello App")

user_name= st.text_input("Your name")
user_dob = st.date_input(
    "Your date of birth", 
    min_value=date(1900, 1, 1), 
    max_value=date.today(), 
    value=date(1990, 1, 1),
    format="DD/MM/YYYY"
    )

if user_name:
    age_days = (date.today() - user_dob).days
    st.write(f"Hello, {user_name.title()}! You have been alive for **{age_days}** days")
    st.write("I thought that would have been a bigger number...")

    

