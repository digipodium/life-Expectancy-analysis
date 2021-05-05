import streamlit as st
import pandas as pd



def viewDataset(path):
    df = pd.read_csv(path)
    st.dataframe(df)


sidebar = st.sidebar
sidebar.header('Choose Your Option')
options = ['View Dataset', 'Analyze By Country','Analyze By Gender','Analyze By Year']
choice = sidebar.selectbox(options= options, label= "Choose Action")

if choice == options[0]:
    st.header('Raw dataset')
    st.info('lifeExpectancyAtBirth.csv -> Life expectancy at birth, country wise mentioned in age (years).')
    viewDataset('datasets/lifeExpectancyAtBirth.csv')
elif choice == options[1]:
    st.image('images/analysisByCountry.png')
    st.image('images/analysisByCountry1.png')
elif choice == options[2]:
    st.image('images/analysisByGender.png')
    st.image('images/analysisByGender1.png')
    st.image('images/pieGender.png')
elif choice == options[3]:
    st.image('images/analysisByYear.png')
    st.image('images/analysisByYear1.png')