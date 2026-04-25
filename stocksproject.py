# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px

company_list = [
    r'/Users/priscilasalgado/Desktop/Proyect 2/individual_stocks_5yr/AAPL_data.csv',
    r'/Users/priscilasalgado/Desktop/Proyect 2/individual_stocks_5yr/AMZN_data.csv',
    r'/Users/priscilasalgado/Desktop/Proyect 2/individual_stocks_5yr/GOOG_data.csv',
    r'/Users/priscilasalgado/Desktop/Proyect 2/individual_stocks_5yr/MSFT_data.csv'
]


all_data = pd.DataFrame()  

for file in company_list:
    current_df = pd.read_csv(file)
    all_data = pd.concat([all_data, current_df], ignore_index=True)

all_data['date'] = pd.to_datetime(all_data['date'])





st.set_page_config(page_title = 'Stock Analysis Dashboard', layout = 'wide' )
st.title('Tech Stocks Analysis Dashboard')

tech_list = all_data['Name'].unique()

st.sidebar.title('Choose a company')


selected_company = st.sidebar.selectbox('Select a stock', tech_list )
company_df = all_data[all_data['Name'] == selected_company].copy()
company_df = company_df.sort_values('date')


##1st plot

st.subheader(f'1. Closing Price of {selected_company} Over Time')
fig1 = px.line(company_df, x = 'date', y = 'close',
        title = selected_company + 'closing prices over time')
st.plotly_chart(fig1, use_container_width=True)

##2nd plot

st.subheader('2. Moving Averages (10,20,50 days)')


ma_day = [10, 20, 50]

for ma in ma_day:
    company_df[f'close_{ma}'] = (
        company_df
        .groupby('Name')['close']
        .transform(lambda x: x.rolling(ma).mean())
    )

fig2 = px.line(company_df, x = 'date', y = ['close_10', 'close_20', 'close_50'],
               title = selected_company + 'closing prices with moving average')


st.plotly_chart(fig2, use_container_width=True)

##3rd plot

st.subheader('3. Daily Returns for ' + selected_company)

company_df['Daily Return (in %)'] = company_df['close'].pct_change() * 100

fig3 = px.line(company_df, x = 'date', y = 'Daily Return (in %)',
               title = 'Daily Return(%)')

st.plotly_chart(fig3, use_container_width=True)


##4th plot

st.subheader('4. Resampled Closing Price (Monthly/ Quarterly, Yearly)')


Resample_option = st.radio('Select Resample Frequency', ['Monthly', 'Quarterly', 'Yearly'])
company_df_resampled = company_df.set_index('date')

if Resample_option == 'Monthly':
    resampled = company_df_resampled['close'].resample('ME').mean()
elif Resample_option == 'Quarterly':
    resampled = company_df_resampled['close'].resample('QE').mean()
else:
    resampled = company_df_resampled['close'].resample('YE').mean()
    
    
fig4 = px.line(resampled,
               title = selected_company + ' ' + Resample_option + 'Average Closing Price')

st.plotly_chart(fig4, use_container_width=True)



# 5th plot - Correlation Heatmap

stocks = all_data.copy()
stocks = stocks.pivot(index='date', columns='Name', values='close')

fig5, ax = plt.subplots()
sns.heatmap(stocks.corr(), annot=True, cmap='coolwarm', ax=ax)

st.pyplot(fig5)

st.markdown('---')
st.markdown('** Note:** This dashboard provides basic technical analysis of major tech stocks using Python and Streamlit')

