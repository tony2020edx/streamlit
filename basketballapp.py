import streamlit as st
import pandas as pd
import numpy as np

path = "/Users/tony/Desktop/datarepo/mortgage_data_repo/Mortgage_sample/price_quote_20220304053409.csv"

df = pd.read_csv(path)



loan_amount_selections = st.sidebar.multiselect('Loan_amount', df['loan_amount'].unique(), default=[300000])
loan_purpose = st.sidebar.multiselect('Loan Purpose', df['loan_purpose'].unique(), default=['Purchase'])
loan_program = st.sidebar.multiselect('Loan Program', df['loan_program'].unique(), default=['FHA'])
data_source = st.sidebar.multiselect('Source', df['source'].unique(), default=['Portal'])
#loan_product = st.sidebar.multiselect('Loan Product', df['product'].unique(), default='30 Yr Fixed')


# loan_ltv = st.sidebar.multiselect('Loan Life Time Value', df['ltv'].unique(), default=[0.8])
# state = st.sidebar.multiselect('State', df['state'].unique(), default='RI')
# credit_score = st.sidebar.multiselect('Credit Score', df['credit_score'].unique(), default=650)


def load_data(data_frame, loan_amount: list, loan_purposes: list, loan_programs: list, data_sources: list):
    new_df = data_frame[
        df.loan_amount.isin(loan_amount_selections) & df.loan_purpose.isin(loan_purpose) & df.loan_program.isin(
            loan_program) & df.source.isin(data_source)]

    return new_df


v1 = load_data(df, loan_amount_selections, loan_purpose, loan_program, data_source)

v1


mortgage_df = df.loc[(df['loan_purpose'] == loan_purpose) & (df['loan_amount'] == loan_amount)]

