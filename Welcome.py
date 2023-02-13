import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')


st.title('PokeDex')
df = pd.read_csv('Pokemon.csv')
st.header('Welcome to your virtual PokeDex!')
from PIL import Image as ime
img = ime.open("pokedex.png")
st.image(img)
if st.button('Click when ready!'):
    st.write('Head over to the Explore tab!')
else:
    pass