# filename: plot_stock_price.py

import datetime
import yfinance as yf
import matplotlib.pyplot as plt

# Get the current date
current_date = datetime.date.today()

# Download stock data
meta_data = yf.download('META', start='2022-01-01', end=current_date)
tesla_data = yf.download('TSLA', start='2022-01-01', end=current_date)

# Plot stock price change for META and TESLA
plt.figure(figsize=(14, 7))
plt.plot(meta_data['Close'], label='META')
plt.plot(tesla_data['Close'], label='TESLA')
plt.title('Stock Price Change YTD for META and TESLA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Save the plot to a file
plt.savefig('stock_price_ytd.png')