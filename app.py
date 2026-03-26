## Streamlit

import streamlit as st
import pandas as pd

# Load the scraped CSV
df = pd.read_csv("Jobs.csv")

# Quick check
st.write("Preview of Data")
st.dataframe(df.head())

import streamlit as st
import pandas as pd

st.title("Data Engineer Jobs Analysis")

# Load CSV
df = pd.read_csv("Jobs.csv")

# Sidebar filters
locations = st.sidebar.multiselect("Select Location", df['Location'].unique())
companies = st.sidebar.multiselect("Select Company", df['Company Name'].unique())
experience_levels = st.sidebar.multiselect("Select Experience", df['Experience'].unique())

# Apply filters
filtered_df = df.copy()
if locations:
    filtered_df = filtered_df[filtered_df['Location'].isin(locations)]
if companies:
    filtered_df = filtered_df[filtered_df['Company Name'].isin(companies)]
if experience_levels:
    filtered_df = filtered_df[filtered_df['Experience'].isin(experience_levels)]

st.write(f"Showing {len(filtered_df)} job listings")
st.dataframe(filtered_df)

import matplotlib.pyplot as plt

location_counts = filtered_df['Location'].value_counts()

st.subheader("Jobs by Location")
st.bar_chart(location_counts)

st.subheader("Jobs by Company")
company_counts = filtered_df['Company Name'].value_counts()
st.bar_chart(company_counts)