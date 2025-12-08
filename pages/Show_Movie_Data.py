import streamlit as st
import pandas as pd

data = pd.read_csv("moviedata.csv")
st.write(data) 
