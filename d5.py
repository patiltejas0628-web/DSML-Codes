import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


st.title("dashboard")

data={
     "names":["a","b","c","d"],
     "marks":[10,20,30,40]
    
}
df=pd.DataFrame(data=data)
st.dataframe(df)