import streamlit as st
import pandas as pd

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database import Report

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

def viewDataset(path):
    df = pd.read_csv(path)
    st.dataframe(df)


def ViewReport():
    reports = sess.query(Report).all()
    titlesList = [ report.title for report in reports ]
    selReport = st.selectbox(options = titlesList, label="Select Report")
    
    reportToView = sess.query(Report).filter_by(title = selReport).first()

    markdown = f"""
        ## {reportToView.title}
        ### {reportToView.desc}
        
    """

    st.markdown(markdown)

sidebar = st.sidebar
sidebar.header('Choose Your Option')
options = ['View Dataset', 'Analyze By Country','Analyze By Gender','Analyze By Year','View Report']
choice = sidebar.selectbox(options= options, label= "Choose Action")

if choice == options[0]:
    viewDataset('datasets/lifeExpectancyAtBirth.csv')
elif choice == options[1]:
    st.image('images/analysisByCountry.png')
    st.image('images/analysisByCountry1.png')
elif choice == options[2]:
    st.image('images/analysisByGender.png')
    st.image('images/analysisByGender1.png')
elif choice == options[3]:
    st.image('images/analysisByYear.png')
    st.image('images/analysisByYear1.png')
elif choice == options[4]:
    ViewReport()