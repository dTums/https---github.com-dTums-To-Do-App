import streamlit as st
from my_email import send_email

st.header("Contact Me")

with st.form(key='email_forms'):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New email from {user_email} 

From : {user_email} 
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your message has been sent. I will get back to you as soon as possible")


