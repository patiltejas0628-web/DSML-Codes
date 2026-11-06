# import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sns
import streamlit as st

st.title("dashboard")

data={
    "names":["amit","priya","rahul","sneha","rohan","neha","pooja","vijay","anjali"],
    "gender":["male","female","male","female","male","female","female","male","female"],
    "subjects":["python","python","java","java","python","java","python","java","python"],
    "marks":[40,50,80,70,60,30,90,60,40],
    "hours":[2,2,4,3,3,3,1,5,3]
}

df=pd.DataFrame(data=data)


gender=st.sidebar.selectbox(
    "enter gender",["All","male","female"]
)

subject=st.sidebar.selectbox(
    "enter subject",["All"]+sorted(df["subjects"].unique().tolist())
)

filtered_data=df.copy()

if gender !="All":
    filtered_data=filtered_data[filtered_data["gender"]==gender]
    
if subject !="All":
    filtered_data=filtered_data[filtered_data["subjects"]==subject]

total_students=len(filtered_data)
maximum_mark=filtered_data["marks"].max()
avg=filtered_data["marks"].mean()
c1,c2,c3=st.columns(3)
st.dataframe(filtered_data)
c1.metric("total students",total_students)
c2.metric("max marks",maximum_mark)
c3.metric("average marks",avg)
