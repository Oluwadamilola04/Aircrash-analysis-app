import os
os.system('pip install matplotlib')
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

def load_data():
    file = 'aircrash.csv'
    df = pd.read_csv(file)
    df['Operator'] = df['Operator'].fillna('Unknown')
    df['Operator'] = df['Operator'].replace('Corporation Aviation National China','China National Aviation Corporation')
    df['Country/Region'] = df['Country/Region'].fillna('Unknown')
    df['Sum of Fatalities(ground)'] = df['Sum of Fatalities(ground)'].replace('vv ','0')
    df['Sum of Fatalities(ground)'] = pd.to_numeric(df['Sum of Fatalities(ground)'])
    df['Total Fatalities'] = df['Sum of Fatalities(ground)'] + df['Sum of Fatalities (air)']
    # Extract year from the date column
    df['Crash Date'] = pd.to_datetime(df['Crash Date'])
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
dfnew = df[(df['Year'] <= to_year) & (from_year <= df['Year'])]

# display metrics
Total_Fatalities = dfnew['Total Fatalities'].sum()
Total_Accidents = dfnew['Aircraft'].count()
Total_Passengers_aboard = dfnew['Sum of Aboard'].sum()
Casualties_ground = dfnew['Sum of Fatalities(ground)'].sum()

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


st.dataframe(dfnew[['Crash Date','Country/Region','Aircraft Manufacturer',
                    'Aircraft','Operator','Sum of Aboard','Total Fatalities']])

# 

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

# horizontal bar chart
try:
    st.header('Top 15 airlines with the most crashes',divider='orange')
    df2 = dfnew['Operator'].value_counts().head(15).sort_values(ascending=True)
    plt.figure(figsize=(10,4))
    plt.barh(df2.index,df2.values,color='#ffaa00')

    for i,value in enumerate(df2.values):
       plt.annotate(str(value),xy=(value,i),
       ha='left',va='center')
    plt.xlabel('Airline')
    plt.ylabel('Number of crashes')
    
    plt.yticks(rotation=0,ha='right')
    plt.show()
    
    st.pyplot(plt)
except ValueError as e:
    st.error(
        """ Error: """ % e.reason
    )

# horizontal bar chart
try:
    st.header(f'Aircraft Models with most number of Accidents',divider='orange')
    df3 = dfnew['Aircraft'].value_counts().head(15).sort_values(ascending=True)
    plt.figure(figsize=(10,4))
    plt.barh(df3.index,df3.values,color='#ffaa00')

    for i,value in enumerate(df3.values):
     plt.annotate(str(value),xy=(value,i),
     ha='left',va='center')
    plt.xlabel('Aircraft')
    plt.ylabel('Number of crashes')
    
    plt.yticks(rotation=0,ha='right')
    plt.show()

    st.pyplot(plt)
except ValueError as e:
    st.error(
        """ Error: """ % e.reason
    )
