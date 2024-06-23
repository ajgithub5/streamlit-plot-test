import pandas as pd
import streamlit as st

if __name__=='__main__':
    
    st.write("Hello Ajay!!! How are you doing.")

    with st.sidebar:
        st.write('Introduction')
        if st.button('Access Data'):
            st.switch_page('pages/data_read.py')

    df = pd.read_csv("pages/data.csv")
    st.write(df)    
    x_axis = st.radio("Select X-Axis",
                      [cols for cols in df.columns],
                    horizontal=True)
    y_axis = st.radio("Select Y-Axis",[cols for cols in df.columns], horizontal=True)
    
    st.write(f"X-Axis --- {x_axis}")
    st.write(f"Y-Axis --- {y_axis}")
    
    st.bar_chart(df, x=x_axis, y=y_axis)