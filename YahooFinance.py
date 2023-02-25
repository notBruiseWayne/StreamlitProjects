import yfinance as yf
import pandas as pd
import streamlit as st

ticker = 'TSlA'
st.write(f"""
## Stocks price
Shown are the stock **closing** prices and ***volume*** for {ticker}
""")
tickerData = yf.Ticker(ticker)
ticker_df=tickerData.history(period='1d', start='2020-12-01', end='2023-02-20')
st.write("""
### Closing prices""")
st.line_chart(ticker_df.Close)
st.write("""
### Volume""")
st.line_chart(ticker_df.Volume)
