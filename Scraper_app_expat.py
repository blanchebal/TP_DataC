import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


st.markdown("<h1 style='text-align: center; color: black;'>EXPAT DATA SCRAPER APP</h1>", unsafe_allow_html=True)

st.markdown("""
This app performs simple webscraping of data from expat-dakar over multiples pages!
* **Python libraries:** base64, pandas, streamlit, requests, bs4
* **Data source:** [Expat-Dakar](https://www.expat-dakar.com/voitures).
""")



# Fonction Background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('img_file2.jpg') 

# Stocker les données dans des variables
Vehicles = pd.read_csv('TP_Group4.csv')

# caching des données
@st.cache_data

def convert_df(df):
    return df.to_csv().encode('utf-8')

def load(dataframe, title, key, key1) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key1):
        # st.header(title)

        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

        csv = convert_df(dataframe)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='Data.csv',
            mime='text/csv',
            key = key)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style.css')        

# Charger les données 
load(Vehicles, 'TP_Group4', '1', '101')
# load(Motocycles, 'Motocycles data', '2', '102')

# Bouton déroulant
# selected_column = st.selectbox('Sélectionnez une colonne', Vehicles.columns)
# st.write(f"Contenu de la colonne '{selected_column}':")
# st.write(df[selected_column])


import streamlit as st
import streamlit.components.v1 as components


components.html("""
    <iframe src="https://ee.kobotoolbox.org/i/kUWU2Twx" width="800" height="600"></iframe>
    """)




 


