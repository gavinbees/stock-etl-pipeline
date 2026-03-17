import extract
import transform
import load

stock_data = extract.get_stock_data()

sector_returns = transform.get_sector_returns(stock_data)
ticker_volatilities = transform.calculate_ticker_volatility(stock_data)
highest_growth = transform.calculate_highest_growth_days(stock_data)
sharpe_ratio = transform.calculate_sharpe(stock_data)
max_drawdowns = transform.calculate_maximum_drawdown(stock_data)
ticker_mapping = transform.ticker_to_sector(stock_data)

load.load_data(sector_returns, ticker_volatilities, highest_growth, sharpe_ratio, max_drawdowns, ticker_mapping)


