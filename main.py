import streamlit as st
import plotly.express as px
from backend import get_data

# add title, text input, slider, select box and sub header
st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ').capitalize()
days = st.slider('Forecast days', min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))

st.subheader(f'{option} for the next {days} days in {place}')
if place:
    # get the temperature/sky data
    filtered_data = get_data(place, days)
    if option == 'Temperature':
        temperatures = [dict['main']['temp'] for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
        # create a temperature plot
        figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
        st.plotly_chart(figure)

    if option == 'Sky':
        sky_condition = [dict['weather'][0]['main'] for dict in filtered_data]
        images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png', 'Rain': 'images/rain.png',
                  'Snow': 'images/snow.png'}
        image_path = [images[condition] for condition in sky_condition]
        st.image(image_path, width=115)
