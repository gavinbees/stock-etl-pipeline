import pandas as pd


#Get the average cumulative sector return over the past year
def get_sector_returns(stock_data: dict):
    sector_returns = {
        "Sector":[],
        "Avg Cumulative Return": []
    }
    for sector in stock_data.keys(): #Each individual sector
        closing_values_sector = stock_data[sector]["Close"] #Get closing values of the sector
        sector_avg = 0
        for ticker in closing_values_sector.columns: #For each ticker in a sector calculate the cumulative return
            sector_avg += (closing_values_sector[ticker].iloc[len(closing_values_sector) -1] / closing_values_sector[ticker].iloc[0]) - 1
        sector_avg /= len(closing_values_sector.columns) #Average out the cumulative return
        sector_returns["Sector"].append(sector)
        sector_returns["Avg Cumulative Return"].append(sector_avg)  #Update dic
    return pd.DataFrame(sector_returns)

#Determine the volatility of each ticker over the trading period
def calculate_ticker_volatility(stock_data: dict):
    ticker_volatility = {
        "Ticker":[],
        "Volatility": []
    }
    for sector in stock_data.keys():
        closing_values_sector = stock_data[sector]["Close"] #Look at closing values for each sector
        for ticker in closing_values_sector.columns: #For each ticker in a sector calculate its annual volatility
            ticker_volatility["Ticker"].append(ticker) 
            ticker_volatility["Volatility"].append(closing_values_sector[ticker].pct_change().std() * (len(closing_values_sector[ticker]) ** 0.5))  
    return pd.DataFrame(ticker_volatility)

#For each sector, find the top day of stock growth
def calculate_highest_growth_days(stock_data: dict):
    sector_growth_days = {
        "Sector": [],
        "Date": [],
        "Average Pct Growth": [] #Average PCT growth is calculated based on the given tickers in a sector, as given by extract.py
    }
    for sector in stock_data:
        sheet = stock_data[sector]["Close"].pct_change().reset_index()#Calculate the percentage change between each day
        sheet['Avg Growth'] = sheet.sum(axis=1, numeric_only=True) / (len(sheet.columns)-1)
        sheet = sheet.sort_values(by="Avg Growth", ascending=False).head(1)
        sector_growth_days["Sector"].append(sector)
        sector_growth_days["Date"].append(str(list(sheet["Date"])[0].date()))
        sector_growth_days["Average Pct Growth"].append(list(sheet["Avg Growth"])[0])
    return pd.DataFrame(sector_growth_days)
    


#Calculate the Sharpe Ratio for each ticker
def calculate_sharpe(stock_data: dict):
    ticker_sharpe_ratios = {
        "Tickers": [],
        "Sharpe Ratio": []
    }
    for sector in stock_data:
        trading_days = len(stock_data[sector])-1
        closing_values = stock_data[sector]["Close"]
        for ticker in closing_values:
            current_ticker = stock_data[sector]["Close"][ticker].pct_change().dropna() #look at pct change day over day  
            daily_sharpe = current_ticker.mean() / current_ticker.std() #Sharpe ratio formula
            sharpe_ratio = daily_sharpe * (trading_days ** 0.5)
            ticker_sharpe_ratios["Tickers"].append(ticker)
            ticker_sharpe_ratios["Sharpe Ratio"].append(sharpe_ratio)

    return pd.DataFrame(ticker_sharpe_ratios)

#Calculate the maximum drawdown over the time period for each ticker
def calculate_maximum_drawdown(stock_data: dict):
    ticker_max_drawdowns = {
        "Tickers": [],
        "Max Drawdown": []
    }
    for sector in stock_data:
        closing_values = stock_data[sector]["Close"]
        for ticker in closing_values:
            ticker_closing_prices = closing_values[ticker]
            rolling_max = ticker_closing_prices.cummax() #Get the rolling/cumulative max
            drawdown = (ticker_closing_prices - rolling_max) / rolling_max #Calculate drawdown
            max_drawdown = drawdown.min() #Get lowest value/max drawdown
            ticker_max_drawdowns["Tickers"].append(ticker)
            ticker_max_drawdowns["Max Drawdown"].append(max_drawdown)
    return pd.DataFrame(ticker_max_drawdowns)
       
#Map each ticker to its sector
def ticker_to_sector(stock_data: dict):
    mapping = {
        "Sector": [],
        "Ticker": []
    }
    for sector in stock_data:
        for ticker in stock_data[sector]["Open"]:
            mapping["Sector"].append(sector)
            mapping["Ticker"].append(ticker)
    return pd.DataFrame(mapping)




         



