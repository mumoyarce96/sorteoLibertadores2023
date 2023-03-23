# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:42:44 2023

@author: Raimundo
"""

import streamlit as st
from sorteoSudamericana import simular, sorteo_a_dataframe
import pandas as pd

st.set_page_config(page_title = "Sorteo Copa Sudamericana 2023")
# CSS to inject contained in a string
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

st.header('Simulación del sorteo de la Copa Sudamericana 2023')
st.subheader('Equipos por bolillero')
b1 = ['Peñarol (Uruguay)',
    'Sao Paulo (Brasil)',
    'Santos (Brasil)',
    'Liga de Quito (Ecuador)',
    'Estudiantes de La Plata (Argentina)',
    'Emelec (Ecuador)',
    'San Lorenzo (Argentina)',
    'Independiente Santa Fe (Colombia)']
b2 = ['Defensa y Justicia (Argentina)',
    'Guaraní (Paraguay)',
    'Bragantino (Brasil)',
    'Universitario (Perú)',
    'Deportes Tolima (Colombia)',
    "Newell's (Argentina)",
    'Botafogo (Brasil)',
    'Palestino (Chile)']
b3 = ['Oriente Petrolero (Bolivia)',
    'Estudiantes de Mérida (Venezuela)',
    'Danubio (Uruguay)',
    'Tigre (Argentina)',
    'América MG (Brasil)',
    'Blooming (Bolivia)',
    'Goiás (Brasil)',
    'Universidad César Vallejo (Perú)']
b4 = [    'Audax Italiano (Chile)',
    'Gimnasia de La Plata (Argentina)',
    'Puerto Cabello (Venezuela)',
    'Tacuary (Paraguay)',
    'Millonarios (Colombia)',
    'Huracán (Argentina)',
    'Fortaleza (Brasil)',
    'Magallanes (Chile)']

dict_bolilleros = {'Bolillero 1': b1,
                   'Bolillero 2': b2,
                   'Bolillero 3': b3,
                   'Bolillero 4': b4}
df_bolilleros = pd.DataFrame(dict_bolilleros)
st.table(df_bolilleros)

if st.button('Sortear grupos'):
    st.subheader('Grupos simulados')
    df_sorteo = sorteo_a_dataframe(simular())
    st.table(df_sorteo[['A', 'B', 'C', 'D']])
    st.table(df_sorteo[['E', 'F', 'G', 'H']])
    st.caption('Se están utilizando las mismas reglas del sorteo 2022: dos equipos del mismo país no pueden compartir grupo. Los equipos provenientes de la Copa Libertadores NO están exentos de esta regla.')