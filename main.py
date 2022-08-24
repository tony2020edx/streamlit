import streamlit as st
import pandas as pd
import numpy as np

path =  "/Users/tony/Desktop/datarepo/mortgage_data_repo/Mortgage_sample/price_quote_20220304053409.csv"

df = pd.read_csv(path)

loan_purpose = st.sidebar.multiselect('Loan Purpose', df['loan_purpose'].unique())
#loan_program = st.sidebar.selectbox('Loan Program', df['loan_program'].unique())
loan_amount = st.sidebar.multiselect('Loan_amount', df['loan_amount'].unique())
#data_source = st.sidebar.selectbox('Source', df['source'].unique())
#loan_product = st.sidebar.selectbox('Loan Product', df['product'].unique())
#loan_ltv = st.sidebar.selectbox('Loan Life Time Value', df['ltv'].unique())
#credit_score = st.sidebar.selectbox('Credit Score', df['credit_score'].unique())
#state = st.sidebar.selectbox('State', df['state'].unique())



@st.cache
def load_data():
    new_df = df.loc[(df.loan_purpose.isin(loan_purpose))&(df.loan_amount.isin(loan_amount))]

    return new_df

new_df_v1 = load_data()
new_df_v1
