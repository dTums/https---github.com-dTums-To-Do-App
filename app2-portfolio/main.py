import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/TumsPhoto.png")

with col2:
    st.title("David Tumaini")
    content = """
     Hi, I'm David, an python programmer as well as an aspiring data analyst. I am also an  
     AWS Certified Cloud Practitioner and have experience with linux, AWS and SQL.
     """
    st.info(content)


content2 = """
Below you can find some of the apps i have built during my python learning process.
Feel free to contact me for any opportunities to work together.
"""

st.write(content2)