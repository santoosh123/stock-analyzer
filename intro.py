import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 Stock Analyzer")

# Ask for stock symbol
symbol = st.text_input("Enter a stock symbol (e.g. AAPL, MSFT, TSLA):", "AAPL")

# Ask for date range
start_date = st.date_input("Start date", pd.to_datetime("2023-01-01"))
end_date = st.date_input("End date", pd.to_datetime("today"))

# Button to fetch data
if st.button("Get Stock Data"):
    try:
        ticker_data = yf.Ticker(symbol)
        ticker_df = ticker_data.history(start=start_date, end=end_date)

        if ticker_df.empty:
            st.warning("No data found for the given range. Try different dates.")
        else:
            st.subheader(f"Stock Price for {symbol}")
            st.line_chart(ticker_df["Close"])
            st.subheader("Raw Data")
            st.write(ticker_df)
    except Exception as e:
        st.error(f"Error fetching data: {e}")
