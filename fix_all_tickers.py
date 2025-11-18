# Add this line after creating your close DataFrame:

# Close prices
close = df_close_adjclose[[c for c in df_close_adjclose.columns if c.endswith("_Close")]].copy()
close.columns = [c.replace("_Close", "") for c in close.columns]

# Adj Close price
adj = df_close_adjclose[[c for c in df_close_adjclose.columns if c.endswith("_AdjClose")]].copy()
adj.columns = [c.replace("_AdjClose", "") for c in adj.columns]

# Sort both by date
close = close.sort_index()
adj = adj.reindex(close.index).sort_index()

# ADD THIS LINE - Define all_tickers from close DataFrame columns
all_tickers = list(close.columns)

print("All tickers:", all_tickers)