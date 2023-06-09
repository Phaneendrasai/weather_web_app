# Importing modules
import pandas as pd
import streamlit as st
import plotly.express as px
from backend import get_data

#Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days of forecasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
#get filtered data
    filtered_data = get_data(place, days)

    #Get the temperature/sky data
    data = get_data(place, days, option)
    d, t = get_data(days)


    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        #Create a temperture plot
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature in (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        st.image()



