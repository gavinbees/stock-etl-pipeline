# Stock Market ETL Pipeline

A Python-based ETL  pipeline that fetches historical stock data for 24 tickers across 5 sectors, calculates financial metrics, and stores everything in a structured SQLite database.

---

## Data Source

All data is fetched from **Yahoo Finance** via the `yfinance` Python library. No API key is required. The pipeline always pulls a trailing 12-month window from the current date, so results are current and reproducible over time. Dates can also be adjusted to any time frame.

---

## Tickers

| Sector | Tickers |
|--------|---------|
| Technology | AAPL, MSFT, NVDA, GOOGL, META, AMD |
| Finance | JPM, BAC, GS, V, BRK-B |
| Healthcare | JNJ, UNH, PFE, ISRG |
| Energy | XOM, CVX, NEE, SLB |
| Consumer | AMZN, WMT, MCD, TSLA |
| Benchmark | SPY |

---

## Key Concepts

**Cumulative Return** — total percentage gain or loss from the start of the period to the end by sector

**Annualized Volatility** — standard deviation of daily returns scaled to a yearly figure

**Highest Growth** - finds the day of highest % growth by sector

**Sharpe Ratio** — return divided by volatility, adjusted for the risk free rate. Measures how much return you earned per unit of risk taken. 

**Maximum Drawdown** — the largest peak to trough drop experienced over the period. Represents the worst case loss for an investor who bought at the worst possible time.


---

## Dependencies

```
yfinance
pandas
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## Notes

- The `/data/stocks.db` file is excluded from version control via `.gitignore`. It is fully regenerated each time `pipeline.py` is run.
- `BRK-B` (Berkshire Hathaway) may occasionally require the alternate format `BRK.B` depending on the yfinance version installed.
- All date ranges are dynamic trailing windows. Running the pipeline today vs. one year from today will produce different results as intended.
