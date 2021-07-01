# import the module
import python_weather
import asyncio
import streamlit as st
import pandas as pd

async def getweather():
    col_1 = []
    col_2 = []
    col_3 = []
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    st.title("My Weather Application :)")
    st.write("This is my weather application. By Pythoholic")
    
    # Option list
    option = st.selectbox(
        "Please choose the name of the city:",
        ("Washington DC", "Chicago", "New York", "New Jersey", "Ohio", "Mumbai", "Hyderabad")
    )
    
    st.write("You choose the city:", option)

    # fetch a weather forecast from a city
    weather = await client.find(option)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        col_1.append(str(forecast.date).split()[0])
        col_2.append(forecast.sky_text)
        col_3.append(forecast.temperature)

    
    st.write(pd.DataFrame({
        "Date" : col_1,
        "Weather" : col_2,
        "Temperature" : col_3
    }))

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError as runex:
        if "There is no current event loop in thread" in str(runex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            asyncio.get_event_loop()
    loop.run_until_complete(getweather())