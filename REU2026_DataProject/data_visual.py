import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image 

# load data
df = pd.read_csv("sleepdata.csv")
df['GDP_per_Capita'] = df['GDP_per_Capita'].astype(str).str.replace(',', '').astype(float)

# title and intro photo
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Georgia', serif;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; font-family: Georgia;'>Why Do We Sleep Earlier?</h1>", unsafe_allow_html=True)

img = Image.open("/Users/charlottelin/Downloads/sleepingimage.png")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(img, width=300)

# spacing: 
st.markdown("<br><br>", unsafe_allow_html=True)

# slide 1- when do we all go to sleep?
st.markdown("<h3 style='text-align: center; font-family: Georgia;'>What time do we all go to sleep?</h1>", unsafe_allow_html=True)

fig_map = px.choropleth(df, 
                        locations='Countries',
                        locationmode='country names',
                        color='Bedtime',
                        color_continuous_scale='RdBu_r',
                        # title='Bedtime Around the World'
                        )

st.plotly_chart(fig_map)

