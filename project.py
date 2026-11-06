import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Train",
    page_icon="🚆",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("passenger .csv")

# Title
st.title("🚆 Train Data Analysis Dashboard")


st.markdown("---")

# Sidebar
st.sidebar.title("Dashboard Filters")

train = st.sidebar.multiselect(
    "Select Train",
    df["Train"].unique(),
    default=list(df["Train"].unique())
)

travel_class = st.sidebar.multiselect(
    "Select Class",
    df["Class"].unique(),
    default=list(df["Class"].unique())
)

gender = st.sidebar.multiselect(
    "Select Gender",
    df["Gender"].unique(),
    default=list(df["Gender"].unique())
)

# Filter Data
data = df[
    (df["Train"].isin(train)) &
    (df["Class"].isin(travel_class)) &
    (df["Gender"].isin(gender))
]

# Dashboard Metrics
st.header("📊 Dashboard Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Passengers", len(data))
c2.metric("Total Trains", data["Train"].nunique())
c3.metric("Total Stations",
          pd.concat([data["From_Station"], data["To_Station"]]).nunique())
c4.metric("Average Age",
          round(data["Age"].mean(), 1) if len(data) else 0)

st.markdown("---")

# Tabs
tab1, tab2, tab3,  = st.tabs([
    "Overview",
    "Train Search",
    "Passenger Analysis",
    
])

# TAB 1: Overview
with tab1:

    st.header("Train Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Passengers by Train")
        st.bar_chart(data["Train"].value_counts())

    with col2:
        st.subheader("Passengers by Class")
        st.bar_chart(data["Class"].value_counts())

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Gender Analysis")
        st.bar_chart(data["Gender"].value_counts())

    with col4:
        st.subheader("Age Category Analysis")
        st.bar_chart(data["Category"].value_counts())


# TAB 2: Train Search
with tab2:

    st.header("🚉 Search Trains")

    stations = sorted(set(df["From_Station"].dropna()) |
                      set(df["To_Station"].dropna()))

    col1, col2 = st.columns(2)

    with col1:
        source = st.selectbox("From Station", stations)

    with col2:
        destinations = [s for s in stations if s != source]
        destination = st.selectbox("To Station", destinations)

    if st.button("Search Train"):

        result = df[
            (df["From_Station"] == source) &
            (df["To_Station"] == destination)
        ]

        if len(result) > 0:
            st.success("Train Records Found!")
            st.dataframe(
                result[["Train", "From_Station",
                        "To_Station", "Class"]].drop_duplicates(),
                use_container_width=True
            )
        else:
            st.warning("No train records found for this route.")

    st.caption("Note: This search uses sample dataset, not live railway information.")


# TAB 3: Passenger Analysis
with tab3:

    st.header("👥 Passenger Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Age Distribution")
        st.bar_chart(data["Age"].value_counts().sort_index())

    with col2:
        st.subheader("Boarding Station Analysis")
        st.bar_chart(data["From_Station"].value_counts())

    st.subheader("Passenger Category")
    st.bar_chart(data["Category"].value_counts())



   



