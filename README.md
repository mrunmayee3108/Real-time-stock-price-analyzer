# ⚡💲💰Real-Time Stock Price Analyzer

A real-time stock market dashboard built using **Streamlit**, **yFinance**, and **Matplotlib**.

This app fetches *live stock prices* in 1-minute intervals and auto-refreshes to give you always-updated market data.


## 🚀 Features

- 📈 **Live price updates** (1-minute interval)
- 🔄 **Auto-refresh timer** (user adjustable from sidebar)
- 💹 **Latest price, high, low & average metrics**
- 🧾 **Live data table** showing recent readings
- 📊 **Live Matplotlib closing price chart**
- 🎨 Clean & responsive UI powered by Streamlit
- 🧩 Works with global stock symbols (AAPL, TSLA, INFY.NS, GOOGL, etc.)


## 📸 Demo Screenshot
<img width="1919" height="852" alt="image" src="https://github.com/user-attachments/assets/18561317-dc78-4dd9-b216-3d436865fc19" />
<img width="1919" height="1015" alt="image" src="https://github.com/user-attachments/assets/b2aeca33-dce9-45c8-a127-5cbebd032636" />
<img width="1919" height="1006" alt="image" src="https://github.com/user-attachments/assets/b84b1ea8-aca2-4388-8048-ab101f079215" />


## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **yFinance**
- **Matplotlib**


## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mrunmayee3108/Real-time-stock-price-analyzer.git
cd Real-time-stock-price-analyzer
```

### 2️⃣ Install required packages

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app

```bash
streamlit run stockprice.py
```

---

## 📁 File Structure

```
Real-time-stock-price-analyzer/
│
├── stockprice.py          # Main Streamlit app
├── requirements.txt       # Required dependencies
├── README.md              # Project documentation

```


## ⚙️ How It Works

1. User enters a stock symbol  
2. App fetches **1-day data at 1-minute intervals** using `yfinance`  
3. UI updates automatically at the chosen refresh interval  
4. Metrics, table, and charts update live  
5. The page auto-reruns using `st.rerun()`  


## 📬 Contributing

Pull requests are welcome!  
If you have ideas for adding:

- Multi-stock comparison  
- Technical indicators (RSI, MACD, MA)  
- Predictive models  

Feel free to open an issue or PR.


## 📝 License

This project is **open-source** and free to use.


## ⭐ Support

If you like this project, consider giving the repository a **⭐ star** on GitHub!


~ Mrunmayee Sachin Potdar

