import yfinance as yf
import matplotlib.pyplot as plt

stock = input("Enter stock symbol (e.g. AAPL, TSLA, INFY.NS): ")
data = yf.download(stock, period="1mo", interval="1d")

plt.plot(data['Close'])
plt.title(f"{stock} - Last 1 Month Closing Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

print("📈 Average price:", round(data['Close'].mean(), 2))
print("🔺 Highest:", round(data['Close'].max(), 2))
print("🔻 Lowest:", round(data['Close'].min(), 2))
