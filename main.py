# INF601 - Advanced Programming in Python
# Bunyamin Sari
# Stremlit Project

import streamlit as st
import yfinance as yf

# Sidebar
my_text = st.sidebar.text_input("Enter a symbol", "AAPL", max_chars=4)

# Main Page
st.header("A simple financial dashboard.")
st.write("An honest trial to learn more about Streamlit.")

# Getting stock data for the specific ticker
stock = yf.Ticker(my_text)

# Image that displays info about the ticker
url = f"https://charts.finviz.com/chart.ashx?t={my_text}"

# Projecting the retrieved image
st.image(url)

# Displays short information about the business
st.subheader("Business Summary")
st.write(stock.info["longBusinessSummary"])

# Retrieving the last 1 month of history and display it
st.subheader("Stock History for the Last 1 Month")
hist = stock.history(period="1mo")
st.write(hist)

# Creating a chart of the history retrieved.
st.subheader("History in Graphics")
st.line_chart(hist)






