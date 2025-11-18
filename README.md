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

📁 Repository Structure
