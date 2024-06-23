import pandas as pd
import streamlit as st

if __name__=='__main__':
    df = pd.read_csv('pages/data.csv')
    with st.expander('Data'):
        st.write(df)


