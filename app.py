import streamlit as st
import pandas as pd

from analyze import Analyse

analysis = Analyse()

def viewDataset(path):
    st.header('Data Used in Project')
    dataframe = analysis.getDataframe()

    with st.spinner("Loading Data..."):
        st.dataframe(dataframe)

        st.markdown('---')
        cols = st.beta_columns(4)
        cols[0].markdown("### No. of Rows :")
        cols[1].markdown(f"# {dataframe.shape[0]}")
        cols[2].markdown("### No. of Columns :")
        cols[3].markdown(f"# {dataframe.shape[1]}")
        st.markdown('---')

        st.header('Summary')
        st.dataframe(dataframe.describe())
        st.markdown('---')

        types = {'object' : 'Categorical', 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], dataframe.dtypes))
        st.header('Dataset Columns')
        for col, t in zip(dataframe.columns, types):
            st.markdown(f"### {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"# {dataframe[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")

sidebar = st.sidebar
sidebar.header('Choose Your Option')
options = ['View Dataset', 'Analyze By Country','Analyze By Gender','Analyze By Year']
choice = sidebar.selectbox(options= options, label= "Choose Action")

if choice == options[0]:
    with st.spinner("Loading Data..."):
        st.header('Raw dataset')
        st.info('lifeExpectancyAtBirth.csv -> Life expectancy at birth, country wise mentioned in age (years).')
        viewDataset('datasets/lifeExpectancyAtBirth.csv')
elif choice == options[1]:
    with st.spinner("Loading Analysis..."):
        st.image('images/analysisByCountry.png')
        st.image('images/analysisByCountry1.png')
elif choice == options[2]:
    with st.spinner("Loading Analysis..."):
        st.image('images/analysisByGender.png')
        st.image('images/analysisByGender1.png')
        st.image('images/pieGender.png')
elif choice == options[3]:
    with st.spinner("Loading Analysis..."):
        st.image('images/analysisByYear.png')
        st.image('images/analysisByYear1.png')