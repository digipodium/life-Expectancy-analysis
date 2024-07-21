import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from analyze import Analyse

st.title('Life Expectancy Analysis')
st.image('2.png')

analysis = Analyse()

sidebar = st.sidebar
sidebar.header('Choose Your Option')
options = ['View Dataset', 'Analyze By Country','Analyze by life Expectancy','Analyze By Gender','Analyze By Year','About']
choice = sidebar.selectbox(options= options, label= "Choose Action")

lifeExpectancy = pd.read_csv('datasets\lifeExpectancyAtBirth.csv')

st.write(lifeExpectancy)

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

def AnalysisByCountry():

    tempData = lifeExpectancy.groupby('Location')['First Tooltip'].mean()
    tempDataTop20 = tempData.sort_values(ascending=False)[:20]
    tempDataLow20 = tempData.sort_values()[:20]
    tempDataTop20 = tempDataTop20.reset_index()
    tempDataLow20 = tempDataLow20.reset_index()
    fig = plt.figure(figsize = (22,10))

    ax1 = plt.subplot2grid((2,1), (0,0), rowspan=1, colspan=1)
    ax1.bar(x = tempDataTop20['Location'], height = tempDataTop20['First Tooltip'], color = "#6ded71")
    ax1.set_xticklabels(tempDataTop20['Location'], rotation=90,size=13)
    ax1.set_ylabel("Life Ecpectancy (Years)",size=15)
    ax1.title.set_text("Top 20 Life Expectancy")    

    ax2 = plt.subplot2grid((2,1), (1,0), rowspan=1, colspan=1)
    ax2.bar(x = tempDataLow20['Location'][::-1], height = tempDataLow20['First Tooltip'][::-1], color = "#f07d73")
    ax2.title.set_text("Bottom 20 Life Expectancy")

    plt.xticks(rotation = 90, size=13)
    plt.xlabel("Countries",size=15)
    plt.ylabel("Life Ecpectancy (Years)",size=15)
    plt.subplots_adjust(hspace = 0.6)
    st.pyplot(fig)

    tempData = lifeExpectancy.groupby('Location')['First Tooltip'].mean()
    tempData = tempData.sort_values(ascending=False)
    tempData = tempData.reset_index()
    tempData.set_index('Location',drop=True,inplace=True)

    countries=['India', 'China', 'United States of America', 'Germany',
            'United Kingdom of Great Britain and Northern Ireland', 
            'Japan', 'Canada']


    ax_1 = tempData['First Tooltip'].plot(kind='bar', title ="Countries v/s Life Expectancy", figsize=(22, 6), fontsize=15)
    ax_1.set_xlabel("Country Name", fontsize=15)
    for ticks in ax_1.xaxis.get_major_ticks():
        if ticks.label1.get_text() not in countries:
            ticks.label1.set_visible(False)
            ax_1.patches[tempData.index.get_indexer([ticks.label1.get_text()])[0]].set_facecolor('w')
            ax_1.patches[tempData.index.get_indexer([ticks.label1.get_text()])[0]].set_edgecolor('#c7c3c3')
        else:
            ax_1.patches[tempData.index.get_indexer([ticks.label1.get_text()])[0]].set_facecolor('r')

    st.pyplot(fig)

    

if choice == options[0]:
    with st.spinner("Loading Data..."):
        st.header('Raw dataset')
        viewDataset('datasets/lifeExpectancyAtBirth.csv')
elif choice == options[1]:
    with st.spinner("Loading Analysis..."):
        st.subheader('Top and bottom 20 life expectancy')
        
        AnalysisByCountry()
        st.subheader('Countries vs life expectancy')
        #CountryVSLifeExpentancy()
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