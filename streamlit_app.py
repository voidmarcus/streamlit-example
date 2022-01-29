import json
import datetime
import requests
import pandas as pd
import streamlit as st

st.write("""
# WhenHarvest AI System
Simulation results are shown for a better harvest!
""")

with st.form(key='my_form'):
    
    with st.sidebar:
        lat = st.text_input('Latitude (°):')
        lng = st.text_input('Longitude (°):')
        whc = st.selectbox(
             'Water holding capacity (mm):',
             ("Coarse sand - 42", "Loamy sandy - 83", "Silt loam - 146", "Heavy clay - 167"))

        sowing = st.date_input('Sowing date:', datetime.date.today())

        submit = st.form_submit_button('Run simulation')

        if submit:
            """
            Selected location:
            """
            df = pd.DataFrame({'lat': [float(lat)], 'lon': [float(lng)]})           
            st.map(df, zoom=8, use_container_width=False)

            dictionary = {'lat':float(lat), 'lng':float(lng), 'sowing':sowing.isoformat(), 'whc':whc}
            input = json.dumps(dictionary, indent = 4)

            base_url = 'https://us-central1-hopeful-grid-336019.cloudfunctions.net/whenharvest-4g?' ## Aqui eu tentei com e sem o ? no final
            response_met_data = requests.get(base_url, input, # <Response [500]>
            #response_met_data = requests.get(base_url, data = input, # <Response [400]>
            verify=True, timeout=400.00)
            content = response_met_data
content # esse objeto esta para ser exibido no container principal da pagina (por isso a msg de erro no inicio de rodar a pagina)
