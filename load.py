import pandas as pd
import sqlite3

def load_data(sector_returns, ticker_volatilities, highest_growth, sharpe_ratio, max_drawdowns, ticker_mapping):
    conn = sqlite3.connect("stocks.db")
    sector_returns.to_sql("sector_returns", conn, if_exists="replace", index=False)
    ticker_volatilities.to_sql("ticker_volatilities", conn, if_exists="replace", index=False)
    highest_growth.to_sql("highest_growth", conn, if_exists="replace", index=False)
    sharpe_ratio.to_sql("sharpe_ratio", conn, if_exists="replace", index=False)
    max_drawdowns.to_sql("max_drawdowns", conn, if_exists="replace", index=False)
    ticker_mapping.to_sql("ticker_mapping", conn, if_exists="replace", index=False)
    
    conn.close()


"""
Below is a python script to run directly in Power BI if you don't want to host the sqlite server

import sqlite3
import pandas as pd
conn = sqlite3.connect(r'....\stocks.db') # Replace with your file path

query = "SELECT * FROM sector_returns" 
sector_returns = pd.read_sql_query(query, conn)

query = "SELECT * FROM ticker_volatilities" 
ticker_volatilities = pd.read_sql_query(query, conn)

query = "SELECT * FROM highest_growth" 
highest_growth = pd.read_sql_query(query, conn)

query = "SELECT * FROM sharpe_ratio" 
sharpe_ratio = pd.read_sql_query(query, conn)

query = "SELECT * FROM max_drawdowns" 
max_drawdowns = pd.read_sql_query(query, conn)

query = "SELECT * FROM ticker_mapping" 
ticker_mapping = pd.read_sql_query(query, conn)

conn.close()

"""
