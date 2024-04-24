import streamlit as st
import pandas as pd
import ydata_profiling 
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(page_title='AutoAnalyze EDA App',layout='wide')

with st.sidebar: 
    st.image("https://lpsonline.sas.upenn.edu/sites/default/files/2022-10/plpso-feratures-data-business.jpg")
    st.title("AutoAnalyze App")
    st.info("This application helps you explore and analyze your data for better understanding and efficiency.")
    st.write("To contribute checkout - github.com/tanush-em")
    
st.title("AutoAnalyze App")

df = None

st.header("Upload your Dataset")
file = st.file_uploader("Upload the dataset in CSV format")
if file:
    df = pd.read_csv(file, index_col=None)
    df.to_csv('dataset.csv', index=None)
    st.text("For a clear view, expand the table window")
    st.dataframe(df)

if st.button("Analyze Data"):
    st.title("Automated Exploratory Data Analysis")
    if df is not None:
        profile_df = df.profile_report()
        st_profile_report(profile_df)
    else:
        st.text("The dataset is not properly uploaded")
        st.text("Upload it and Try again !")
    
