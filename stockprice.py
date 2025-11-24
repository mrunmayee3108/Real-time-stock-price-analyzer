import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import time
st.set_page_config(page_title="Real time stock price analyser", layout = "wide")
st.title("Real Time Stock Price Analyser⚡⚡")
refresh_rate = st.sidebar.slider("Auto refresh every (seconds)", 5, 10, 60)
st.sidebar.write("App will refresh automatically⌚")
stock = st.text_input("Enter stock symbol (eg. AAPL, TSLA, INFY.NS, GOOGL): ", "GOOGL")
placeholder = st.empty()
while True:
    with placeholder.container():
        if stock:
            st.subheader(f"Live data for **{stock}**📈📉")
            data = yf.download(stock, period = "1d", interval = "1m")
            if data.empty:
                st.error("Invalid stock symbol or data unavailable!☹️")
                time.sleep(refresh_rate)
                st.rerun()
            else:
                latest_price = round(data['Close'].iloc[-1], 2)
                st.metric(label = "💲Latest Price:", value = latest_price)
                st.subheader("Latest data (Auto updating)")
                st.dataframe(data.tail())
                st.subheader("Live charts (1 min interval)")
                fig, ax = plt.subplots()
                ax.plot(data['Close'])
                ax.set_title(f"{stock} Live Price(today)")
                ax.set_xlabel("Time")
                ax.set_ylabel("Price")
                st.pyplot(fig)
                st.subheader("Today's key stats📊")
                col1, col2, col3 = st.columns(3)
                col1.metric("Highest today", round(data['High'].max(), 2))
                col2.metric("Lowest today", round(data['Low'].min(), 2))
                col3.metric("Average today", round(data['Close'].mean(), 2))
        else:
            st.warning("Enter a stock symbol to begin")
    time.sleep(refresh_rate)
    st.rerun()


