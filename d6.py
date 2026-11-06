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
minimum=st.slider("enter marks",1,100,10)
actual_data=df[df["marks"]>minimum]
st.dataframe(actual_data)


