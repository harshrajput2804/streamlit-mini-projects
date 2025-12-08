import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv("moviedata.csv")
st.write(data) 


st.write("# My Chart Demo") 

chart_data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["a", "b", "c"]
)
st.bar_chart(chart_data)
st.line_chart(chart_data)