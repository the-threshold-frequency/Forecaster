import streamlit as st
import plotly.express as px
from backend import get_data

st.title("PJ's Weather Forecaster")
place = st.text_input("Place: ", placeholder="Enter the name of the place...")
days = st.slider("No. of Days to Forecast: ", min_value=1, max_value=5)
option = st.selectbox("Check Temperature or Sky: ", ("Temperature", "Sky"))

if place:

    try:
        date, temperature, sky, t, w, min, max = get_data(place, days)
        t = "{:.2f}".format(t)
        max = "{:.2f}".format(max)
        min = "{:.2f}".format(min)
        st.header(f"Current Temperature in {place}:")
        st.subheader(f"{t}°C ({w.title()})")
        figure = px.line(x=date, y=temperature, labels={"x": "date", "y": "Temperature (C)"})
        if option == "Temperature":
            st.header(f"{option} for {days} day/s in {place}")
            st.info("Forecast readings are in 3 hour intervals for each day")
            st.plotly_chart(figure)
        if option == "Sky":
            st.subheader(f"{option} for {days} day/s in {place}")
            imagepath = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                         "Snow": "images/snow.png"}
            image = [imagepath[i] for i in sky]
            st.image(image, width=115)
    except (KeyError, NameError):
        st.info("Sorry, I could not find the place you entered :(")



