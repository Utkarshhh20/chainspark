import pandas as pd
import yfinance as yf

# Load your CSV file
file_path = r'C:\\Users\\Utki\Desktop\\code\\blockchain defi project\\frontend\blockchain-marketplace\\src\\components\\Filtered_Currency_Data.csv'
currency_df = pd.read_csv(file_path)

# List of currency codes
currency_codes = currency_df['currency code'].tolist()

# Function to get market cap from Yahoo Finance
def get_market_cap(ticker):
    try:
        stock = yf.Ticker(ticker)
        market_cap = stock.info.get('marketCap', None)
        return market_cap
    except Exception as e:
        return None

# Get market cap for each currency
market_caps = []
for code in currency_codes:
    market_cap = get_market_cap(code + "-USD")
    market_caps.append(market_cap)

# Add the market cap data to the dataframe
currency_df['market cap'] = market_caps

# Filter out coins with market cap below 1 million
filtered_currency_df = currency_df[currency_df['market cap'] >= 1000000]

filtered_file_path = r'C:\\Users\\Utki\Desktop\\code\\blockchain defi project\\AI\\crypto_tickers.csv'
filtered_currency_df.to_csv(filtered_file_path, index=False)
# Display the filtered dataframe
filtered_currency_df.head()