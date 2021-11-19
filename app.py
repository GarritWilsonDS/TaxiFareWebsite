#from datetime
import datetime

import streamlit as st
import requests
import pandas as pd
import pytz

'''
# TaxiFareModel front
'''

st.markdown('''# Welcome to the Taxi Fare Prediction Challenge

## On this website you'll be asked to input certain factors influencing the price of a taxi fare in NY.

##### Our model will then give a prediction of the expected fare price, so you can plan accordingly. Enjoy!
''')

st.markdown("##### For the prediction we will need the following information from you:")

d = st.date_input("daaaaaate")
t = st.time_input('tiiiiiime', datetime.time(8, 45))
pickup_datetime = f'{d} {t}'
st.write(pickup_datetime)
pickup_longitude = st.number_input("pickup longitude")
pickup_latitude = st.number_input("pickup latitude")
dropoff_longitude = st.number_input("dropoff longitude")
dropoff_latitude = st.number_input("dropoff latitude")
passenger_count = st.number_input("passenger count")

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    key_ = "2013-07-06 17:18:00.000000119"

    dict_ = {
        "key": key_,
        "pickup_datetime": [pickup_datetime],
        "pickup_longitude": [float(pickup_longitude)],
        "pickup_latitude": [float(pickup_latitude)],
        "dropoff_longitude": [float(dropoff_longitude)],
        "dropoff_latitude": [float(dropoff_latitude)],
        "passenger_count": [int(passenger_count)]
    }

    response = requests.get(url, params= dict_).json()


    st.markdown(f"## Predicted Taxi Fare: \n {response['prediction']}")
