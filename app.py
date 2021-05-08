import streamlit as st
import pandas as pd

from analyze import Analyse

st.title('Life Expectancy Analysis')
st.image('2.png')

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
options = ['View Dataset', 'Analyze By Country','Analyze by life Expectancy','Analyze By Gender','Analyze By Year','About']
choice = sidebar.selectbox(options= options, label= "Choose Action")

if choice == options[0]:
    with st.spinner("Loading Data..."):
        st.header('Raw dataset')
        viewDataset('datasets/lifeExpectancyAtBirth.csv')
elif choice == options[1]:
    with st.spinner("Loading Analysis..."):
        st.subheader('Top and bottom 20 life expectancy')
        st.image('images/analysisByCountry.png')
        st.subheader('Countries vs life expectancy')
        st.image('images/analysisByCountry1.png')
        st.image('images/analysisByRegion.png')
        st.image('images/analysisByRegion1.png')
        st.image('images/analysisByRegion2.png')
        st.image('images/analysisByRegion3.png')
elif choice == options[2]:
    with st.spinner("Loading Analysis..."):
        st.image('images/analysisByExpectancy.png')
        st.image('images/analysisByExpectancy1.png')
elif choice == options[3]:
    with st.spinner("Loading Analysis..."):
        st.subheader('Top difference between life expectancy of male and female')
        st.image('images/analysisByGender.png')
        st.subheader('Progress in male and female life expectancy of male and female')
        st.image('images/analysisByGender1.png')
        st.subheader('Total percentage of male and female and both sexes')
        st.image('images/pieGender.png')
        st.image('images/analysisByGender2.png')
elif choice == options[4]:
    with st.spinner("Loading Analysis..."):
        st.subheader('Top difference between life expectancy of both sexes')
        st.image('images/analysisByYear.png')
        st.subheader('Progress in life expectancy from 2010 to 2019')
        st.image('images/analysisByYear1.png')
        st.subheader('Progress in life expectancy of male and feamle over years')
        st.image('images/analysisByYear2.png')
elif choice == options[5]:
    with st.spinner("Loading Analysis..."):
        st.write('''Life expectancy is a statistical measure of the average time an organism is expected to live, based on the year of its birth, its current age, and other demographic factors including biological sex. The most commonly used measure is life expectancy at birth (LEB), which can be defined in two ways. Cohort LEB is the mean length of life of an actual birth cohort (all individuals born in a given year) and can be computed only for cohorts born many decades ago so that all their members have died. Period LEB is the mean length of life of a hypothetical cohort assumed to be exposed, from birth through death, to the mortality rates observed at a given year.
        ''')
        st.write('Here, in this project life expectancy of different countries over a period of time is measured, analyzed, graphs put together, and raw dataset used is displayed for better insights by user')