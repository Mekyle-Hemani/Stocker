import yfinance as yf

def grab(stock):
    stockData = yf.Ticker(stock)
    latestPrice = stockData.history(period="1d")['Close'].iloc[-1]
    return (f"Latest price of {stock}: ${latestPrice:.2f}")