# INF601 - Advanced Programming in Python
# Bunyamin Sari
# Stremlit Project

import streamlit as st
import yfinance as yf

my_text = st.sidebar.text_input("Enter a symbol", "AAPL", max_chars=4)
st.header("A simple financial dashboard.")
st.write("An honest trial to learn more about Streamlit. ")


stock = yf.Ticker(my_text)

url = f"https://charts.finviz.com/chart.ashx?t={my_text}"

st.image(url)
st.write(stock.info["longBusinessSummary"])

hist = stock.history(period="1mo")
st.write(hist)
st.line_chart(hist)






