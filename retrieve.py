import yfinance as yf

def grab(stock):
    apple = yf.Ticker(stock)
    latest_price = apple.history(period="1d")['Close'].iloc[-1]
    print(f"Latest price of {stock}: ${latest_price:.2f}")