#Import Libraries
import streamlit as st
import plotly.express as px
import pandas as pd

#Import data set
st.title("TimeLine of Corona Reported Cases Based On Country Selected ")
df=pd.read_csv('full_grouped.csv')
st.subheader("Data overview")
st.write(df)

#st.write(df.head())
st.title("Columns")
st.write(df.columns)

#Summary stats
st.subheader("Statical Information")
st.write(df.describe())

#Data managment on the based of Country selection
country_option=df['Country/Region'].unique().tolist()
country=st.selectbox("Select your Country for Corona cases history?" ,country_option,0)
df=df[df['Country/Region']==country]

#Plotting
# Animation bars chart covid cases changes

fig = px.bar(df, x="Country/Region", y="Confirmed", color="Country/Region",
  animation_frame="Date", animation_group="Country/Region", range_y=[0,df['Confirmed'].max() + 100000])
st.write("Timeline of Confirmed Cases")
fig

#Comparison of cases on the basis of grouped countries
#Data Managment
full_grouped = pd.read_csv('full_grouped.csv')

india = full_grouped[full_grouped['Country/Region'] == 'India']
Pak = full_grouped[full_grouped['Country/Region'] == 'Pakistan']
russia = full_grouped[full_grouped['Country/Region'] == 'Russia']
china = full_grouped[full_grouped['Country/Region'] == 'China']
df1 = pd.concat([india,Pak,russia,china], axis=0)

#Plotting
fig1 = px.bar(df1, x="Country/Region", y="Confirmed", color="Country/Region",
  animation_frame="Date", animation_group="Country/Region", range_y=[0,df['Confirmed'].max() + 100000])
fig1