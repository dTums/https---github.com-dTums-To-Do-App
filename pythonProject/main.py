import streamlit as st
import pandas as pd

st.header("The Best Company")

st.write("This the best company to work with, to work for and to get your goods and services from")

st.subheader("Our Team")
#prepare the columns
col1, empty_col1, col2, empty_col2, col3 = st.columns([1, 0.3, 1, 0.3, 1])
#load the dataframe with co. members
df = pd.read_csv('data-2.csv')
#add content to the columns
with col1:
    for index, row in df[:4].iterrows():
        #st.subheader(row['first name'] + " " + row['last name']) -- or better
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row['role'])
        st.image('images-2/' + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row['role'])
        st.image('images-2/' + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row['role'])
        st.image('images-2/' + row['image'])

