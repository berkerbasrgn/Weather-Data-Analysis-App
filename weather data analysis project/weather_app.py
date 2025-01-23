import streamlit as st
import pandas as pd
import plotly.express as px

data = {
    'Date': pd.date_range(start='2023-01-01', periods=365, freq='D'),
    'Temperature (°C)': [15 + 10 * (i % 30) / 30 for i in range(365)],
}


df = pd.DataFrame(data)
df.set_index('Date', inplace=True)
df['temp_increased'] = df['Temperature (°C)'] + 2  # Simple increase of 2°C
df['Month'] = df.index.month



monthly_means = df.groupby('Month')[['Temperature (°C)', 'temp_increased']].mean().reset_index()



fig = px.line(monthly_means, x='Month', y=['Temperature (°C)', 'temp_increased'],
              title='Monthly Mean Temperature vs. Temperature Increased',
              labels={'value': 'Temperature (°C)', 'variable': 'Column'},
              markers=True)
fig.update_layout(xaxis_title='Month', yaxis_title='Temperature (°C)', template='plotly_white')



st.title("weather data analysis")
st.header("original data")
st.write(df)
st.header("monthly mean temp")
st.write(monthly_means)
st.header("monthly mean temp vs temp increased")
st.plotly_chart(fig)
