import streamlit as st
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt # type: ignore

def load_data():
    file = 'Air__Crash.xlsx'
    df = pd.read_excel(file,engine='openpyxl')
    df['Operator'] = df['Operator'].fillna('Unknown')
    df['Operator'] = df['Operator'].replace('Corporation Aviation National China','China National Aviation Corporation')
    df['Country/Region'] = df['Country/Region'].fillna('Unknown')
    df['Sum of Fatalities(ground)'] = df['Sum of Fatalities(ground)'].replace('vv ','0')
    df['Sum of Fatalities(ground)'] = pd.to_numeric(df['Sum of Fatalities(ground)'])
    df['Total Fatalities'] = df['Sum of Fatalities(ground)'] + df['Sum of Fatalities (air)']
    # Extract year from the date column
    df['Year'] = df['Crash Date'].dt.year

    return df


## load the dataset
df = load_data()
#app title
st.title('Aircrash analysis app')

# insert a slider to filter through the years
min_value = df['Year'].min()
max_value = df['Year'].max()

from_year, to_year = st.slider(
    'Which years are you interested in?',
    min_value=min_value,
    max_value=max_value,
    value=[min_value, max_value])

# display the table
#st.dataframe(df.head(100))


# display metrics
Total_Fatalities = df['Total Fatalities'].sum()
Total_Accidents = df['Aircraft'].count()
Total_Passengers_aboard = df['Sum of Aboard'].sum()
Casualties_ground = df['Sum of Fatalities(ground)'].sum()

st.subheader('Key Numbers')
col1, col2, col3, col4 = st.columns(4)

col1.metric('Total Fatalities', Total_Fatalities)
col2.metric('Total Accidents', Total_Accidents)
col3.metric('All time passengers', Total_Passengers_aboard)
col4.metric('Total ground casualties', Casualties_ground)

# end of metrics
''
''
# display the filtered table
st.dataframe(df)

# 
dfnew = df[(df['Year'] <= to_year) & (from_year <= df['Year'])]
# area chart
try:
    st.header(f'Yearly trend of Fatalities',divider='orange')
    ''
    area1 = dfnew.groupby(['Year'])['Total Fatalities'].sum()
    st.area_chart(area1,color='#ffaa00')
except ValueError as e:
    st.error(
        """ Error: """ % e.reason
    )

# line chart
try:
    st.header(f'Aircrash trends over the years',divider='orange')
    line1 = dfnew.groupby('Year')['Aircraft'].count()
    st.area_chart(line1,color='#ffaa00')
except ValueError as e:
    st.error(
        """ Error: """ % e.reason
    )
