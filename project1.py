
import streamlit as st
import pandas as pd

st.title("Train Dashboard 🚆")

# Train dataset
data = {
    "Train_No": [101, 102, 103, 104, 105],
    "Train_Name": ["Deccan Express", "Sahyadri Express",
                   "Mahalaxmi Express", "Intercity Express",
                   "Shatabdi Express"],
    "From": ["Mumbai", "Pune", "Mumbai", "Kolhapur", "Pune"],
    "To": ["Pune", "Kolhapur", "Nagpur", "Pune", "Mumbai"],
    "Departure": ["08:00", "09:00", "10:00", "11:00", "12:00"],
    "Arrival": ["11:30", "12:00", "18:00", "14:00", "15:30"],
    "Fare": [250, 150, 500, 200, 300]
}

df = pd.DataFrame(data)

# Select locations
st.sidebar.header("Search Your Train")

from_station = st.sidebar.selectbox(
    "Select Location",
    ["From Station"]+sorted(df["From"].unique())
)

to_station = st.sidebar.selectbox(
    "Select Location",
    ["To Station"]+sorted(df["To"].unique())
)

# Search button
if st.sidebar.button("Search Train"):

    result = df[
        (df["From"] == from_station) &
        (df["To"] == to_station)
    ]

    if len(result) > 0:
        st.success("Train Found!")

        st.dataframe(result)

    else:
        st.error("No Train Available")

# Complete train information
st.header("All Train Details")
st.dataframe(df)

# Data Analysis
st.header("Train Data Analysis")

st.write("Total Trains:", len(df))

st.write("Average Fare:", df["Fare"].mean())

st.write("Highest Fare:", df["Fare"].max())

st.write("Lowest Fare:", df["Fare"].min())

# Graph
st.header("Train Fare Chart")

st.bar_chart(df, x="Train_Name", y="Fare")
