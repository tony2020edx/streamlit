import streamlit as st
import pandas as pd
import numpy as np
import time

path = "/Users/tony/PycharmProjects/streamlit/washing_machines_cleaned.csv"

header = st.container()
data = st.container()
filters = st.container()
graphs = st.container()

df = pd.read_csv(path)

with header:
    st.title("Washing Machine Data Analysis")
    st.text("This is a data analysis app for washing machines.")

with data:
    st.title("The Washing machine Data")
    st.write(df.head(10))

with filters:
    brand = st.sidebar.multiselect('Brand', df['brand'].unique())
    type_of_washing = st.sidebar.multiselect('Type of Washing', df['Type_of_washing'].unique())
    star_rating = st.sidebar.slider('Thrushold', min_value=0.0, max_value=5.0, value=0.5, step=0.1)

    sale_price = st.sidebar.slider('Pricing', 0, 100, (0, df['Sale_price'].max()))
    mrp = st.sidebar.slider('MRP', 0, 100, (0, df['MRP'].max()))
    discount_percentage = st.sidebar.slider('Discount Percentage', 0, 100, (0, 100))
    number_of_ratings = st.sidebar.slider('Number of Ratings', 0, 100, (0, df['Number_of_ratings'].max()))
    number_of_reviews = st.sidebar.slider('Number of Reviews', 0, 100, (0, df['Number_of_reviews'].max()))

with graphs:
    pricing_distribution = df['Sale_price'].value_counts().head(50)
    st.bar_chart(pricing_distribution)