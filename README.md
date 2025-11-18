DS637 Midterm Project — Stock Portfolio Simulation (2018)

This repository contains my midterm project for DS 637 – Applied Statistics as part of the MS in Data Science program at NJIT.
The goal of this project is to build a complete stock portfolio simulation system using Python, covering returns, rebalancing, correlations, dividends, and performance visualization.

📊 Project Overview

The portfolio consists of 10 major equities, each starting with an initial investment of $1,000,000 on January 2, 2018:

IBM

MSFT

GOOG

AAPL

AMZN

NFLX

ORCL

SAP

TSLA

WMT

The analysis uses daily stock prices from 2018 and includes:

✔️ Daily returns
✔️ Cumulative returns
✔️ 5-day rebalancing logic
✔️ Buy-low adjustments (e.g., 2018-01-09)
✔️ Dividend capture logic (e.g., IBM on 2018-02-08)
✔️ Rolling correlations
✔️ Portfolio value tracking
✔️ Visualizations and summary statistics

🔧 Technologies & Libraries

The project is implemented in Python using:

Pandas

NumPy

Matplotlib / Seaborn

yfinance or CSV-based price data

Jupyter Notebook

/
│
├── notebooks/
│   └── DS637_Midterm.ipynb
│
├── data/
│   ├── aapl.csv
│   ├── amzn.csv
│   ├── msft.csv
│   └── ...etc
│
├── images/
│   ├── cumulative_returns.png
│   ├── correlations_heatmap.png
│   └── portfolio_value.png
│
└── README.md

📈 Key Components
1️⃣ Data Wrangling

Importing daily OHLC data

Aligning date indexes

Fixing missing values

Merging into a single DataFrame

2️⃣ Return Calculations

Daily returns

Log returns

Rolling averages

3️⃣ Portfolio Simulation

Initial allocation = $1,000,000 per stock

Shares = investment ÷ price

Daily value tracking

4️⃣ Rebalancing

Automated 5-day cycle:

Buy positions that dropped

Sell positions that increased

Reallocate to maintain weights

5️⃣ Dividends

Example:

IBM dividend on 2018-02-08

Captured and reinvested

6️⃣ Correlation Analysis

Examines relationships across the 10-stock basket:

Correlation matrix

Heatmap

Rolling 30-day correlations

📌 Results Summary

Key observations from the simulation:

Several tech stocks (AMZN, NFLX, AAPL) showed strong momentum in early 2018.

Tesla and IBM demonstrated higher volatility.

Correlations among large-cap tech stocks were notably high.

Rebalancing helped smooth fluctuations in portfolio value.

(Full details in the notebook.)
