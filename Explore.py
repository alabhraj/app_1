import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')

df = pd.read_csv('Pokemon.csv')
by_type1 = df.value_counts('Type 1')
bt1 = by_type1.to_frame()
bt1.reset_index(inplace = True)
bt1.rename(columns = {0: 'num'}, inplace = True)
by_type1_fig = px.bar(bt1, x = 'Type 1', y = 'num', color = 'num', labels = {'num': 'number of pokemons', 'Type 1': 'Primary Type'})

g2 = df.groupby(['Type 1', 'Type 2'])
df2 = g2.size().to_frame()
df2.reset_index(inplace = True)
df2.rename(columns = {0: 'num'}, inplace = True)
by_types_fig = px.bar(df2, x = 'Type 1', y = 'num', color = 'Type 2', labels = {'num': 'number of pokemons', 'Type 1': 'Primary Type'})


with st.expander('Pokemon by Type'):
    check_names = ['By Primary Type', 'By Combined Types']
    f1 = st.radio('Filter', check_names)
    if f1 == 'By Primary Type':
        by_type1_fig
    elif f1 == 'By Combined Types':
        by_types_fig
    else:
        pass

gen = df.value_counts('Generation').to_frame()
gen.reset_index(inplace = True)
gen.rename(columns = {0: 'num'}, inplace = True)
gen.replace([1, 2, 3, 4, 5, 6], ['Gen 1', 'Gen 2', 'Gen 3', 'Gen 4', 'Gen 5', 'Gen 6'], inplace = True)
gen.sort_values('Generation', inplace = True)
gen_fig = px.pie(gen, values = 'num', names = 'Generation').update_traces(textposition = 'inside', textinfo = 'percent+label')
with st.expander('Pokemon by Generation'):
    gen_fig

df5 = pd.read_csv('pages\pokemongo.csv')
cap_rate = px.bar(df5, x = 'name', y = 'capture_rate')
flee_rate = px.bar(df5, x = 'name', y = 'flee_rate')
stats_fig_comb = px.bar(df5, x = 'name', y = ['stamina', 'atk', 'def'])
with st.expander('Pokemon by Stats'):
    stats_fig_comb

with st.expander('Pokemon on Confrontation'):
    filter_2 = ['Capture Rate', 'Flee Rate']
    f2 = st.radio('On Confrontation', filter_2)
    if f2 == 'Capture Rate':
        cap_rate
    elif f2 == 'Flee Rate':
        flee_rate
    else:
        pass