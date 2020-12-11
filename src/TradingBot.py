import pandas as pd
import pandas_datareader as pdr
import datetime

# Import from Google Finance
import quandl
aapl = quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")

# Import from Yahoo Finance
aapl = pdr.get_data_yahoo('AAPL',
                          start=datetime.datetime(2005, 10, 1),
                          end=datetime.datetime(2020, 12, 1))

print("aapl.tail()")
print(aapl.tail())

print("aapl.head()")
print(aapl.head())

print("aapl.describe()")
print(aapl.describe())

print("aapl.index")
print(aapl.index)

print("aapl.columns")
print(aapl.columns)

print("aapl.Close")
print(aapl.Close)

print('Time Sample')
ts = aapl['Close'][-10:]
print(ts)
print(type(ts))


# You can pass the label of the row labels, such as 2007 and 2006-11-01, to the loc()
# function, while you pass integers such as 22 and 43 to the iloc() function.

# Inspect the first rows of November-December 2006
print(aapl.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')].head())
# Inspect the first rows of 2007
print(aapl.loc['2007'].head())
# Inspect November 2006
print(aapl.iloc[22:43])
# Inspect the 'Open' and 'Close' values at 2006-11-01 and 2006-12-01
print(aapl.iloc[[22,43], [0, 3]])

aapl.to_csv('../data/aapl_ohlc.csv')
df = pd.read_csv('../data/aapl_ohlc.csv', header=0, index_col='Date', parse_dates=True)


print("This is TradingBOT")