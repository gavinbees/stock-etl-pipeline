import yfinance as yf
from datetime import datetime, timedelta

def get_date_range(days=365):
    end = datetime.today()
    start = end - timedelta(days=days)
    return start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")


def get_stock_data():

    tickers = {
    "Technology": ["AAPL", "MSFT", "NVDA", "GOOGL", "META", "AMD"],
    "Finance": ["JPM", "BAC", "GS", "V", "BRK-B"],
    "Healthcare": ["JNJ", "UNH", "PFE", "ISRG"],
    "Energy": ["XOM", "CVX", "NEE", "SLB"],
    "Consumer": ["AMZN", "WMT", "MCD", "TSLA"],
    "Benchmark/S&P": ["SPY"]
    }

    start, end = get_date_range()
    for key in tickers.keys():
        tickers[key] = yf.download(tickers[key], start=start, end=end)
    return tickers

