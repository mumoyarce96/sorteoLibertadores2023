# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 18:36:13 2023

@author: Raimundo
"""

import streamlit as st
from sorteoLibertadores import simular, sorteo_a_dataframe
import pandas as pd

st.set_page_config(page_title = "Sorteo Copa Libertadores 2023")
# CSS to inject contained in a string
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

st.header('Simulación del sorteo de la Copa Libertadores 2023')
st.subheader('Equipos por bolillero')
b1 = ['Flamengo (Brasil)', 'River Plate (Argentina)', 'Palmeiras (Brasil)',
                                   'Boca Juniors (Argentina)', 'Athletico Paranaense (Brasil)',
                                   'Nacional (Uruguay)', 'Independiente del Valle (Ecuador)',
                                   'Olimpia (Paraguay)']
b2 = ['Libertad (Paraguay)', 'Atlético Nacional (Colombia)',
                                   'Internacional (Brasil)', 'Barcelona (Ecuador)', 
                                   'Racing (Argentina)', 'Corinthians (Brasil)',
                                   'Colo Colo (Chile)', 'Fluminense (Brasil)']
b3 = ['Bolívar (Bolivia)', 'The Strongest (Bolivia)', 
                                   'Melgar (Perú)', 'Alianza Lima (Perú)', 
                                   'Argentinos Juniors (Argentina)', 'Metropolitanos (Venezuela)',
                                   'Aucas (Ecuador)', 'Monagas (Venezuela)']
b4 = ['Liverpool (Uruguay)', 'Deportivo Pereira (Colombia)', 'Ñublense (Chile)',
      'Patronato (Argentina)', 'Atlético Mineiro (Brasil)*', 
      'Sporting Cristal (Perú)*', 'Cerro Porteño (Paraguay)*',
      'Independiente Medellín (Colombia)*']

dict_bolilleros = {'Bolillero 1': b1,
                   'Bolillero 2': b2,
                   'Bolillero 3': b3,
                   'Bolillero 4': b4}
df_bolilleros = pd.DataFrame(dict_bolilleros)
st.table(df_bolilleros)
st.caption('*Equipo clasificado desde la Fase Previa')

    

if st.button('Sortear grupos'):
    st.subheader('Grupos simulados')
    df_sorteo = sorteo_a_dataframe(simular({'Flamengo': 'A'}))
    st.table(df_sorteo[['A', 'B', 'C', 'D']])
    st.table(df_sorteo[['E', 'F', 'G', 'H']])
