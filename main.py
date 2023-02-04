import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place:')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

if place:
    try:
        data = get_data(place, days)

        if option == 'Temperature':
            temp = [dict['main']['temp'] - 273.15 for dict in data]
            date = [dict['dt_txt'] for dict in data]
            figure = px.line(x=date, y=temp, labels={'x': 'Date', 'y': 'Temperature (c)'})
            st.plotly_chart(figure)

        if option == 'Sky':
            sky_conditions = [dict['weather'][0]['main'] for dict in data]
            images = {'Clear': 'images/clear.png',
                      'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png',
                      'Snow': 'images/snow.png'}
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width=115)
    except KeyError:
        st.write("This place dose not exist!")
