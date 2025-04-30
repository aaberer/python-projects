import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import pandas as pd

# rsi method


def rsi(df, periods):
    # change in cell values
    close_delta = df['Close'].diff()

    # removing any exponants
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)

    # exponetial rolling averages used
    MA_up = up.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
    MA_down = down.ewm(com=periods - 1, adjust=True,
                       min_periods=periods).mean()

    rsi = MA_up / MA_down
    rsi = 100 - (100/(1 + rsi))
    return rsi


def cash_to_BTC(holdings_in_cash, close_price):
    return holdings_in_cash / close_price


def BTC_to_cash(holdings_in_BTC, close_price):
    return holdings_in_BTC * close_price


def run():
    df = pd.read_csv(r'BTCUSD_day.csv', index_col=0,
                     parse_dates=True, usecols=['Date', 'Close'])
    rsi_data = rsi(df, 14)
    # Calculate the 50 day moving average
    MA_50 = df['Close'].rolling(window=50).mean()
    df['MA_50'] = MA_50  # Add the new column to the dataframe
    # Calculate the 20 day moving average
    MA_20 = df['Close'].rolling(window=20).mean()
    df['MA_20'] = MA_20  # Add the new column to the dataframe
    df = df.dropna()

    buy_list = []
    sell_list = []
    # sort the dataframe by date from oldest date to current date
    df = df.sort_values(by='Date')

    # Loop through the dataframe. iloc is used to access the data at a specific index (row)
    for i in range(len(df)):
        # If the 20 day moving average is greater than the 50 day moving average and the 20 day moving average was less than the 50 day moving average on the previous day
        if df.MA_20.iloc[i] > df.MA_50.iloc[i] and df.MA_20.iloc[i-1] < df.MA_50.iloc[i-1]:
            # Add the index of the buy signal to the Buy list
            buy_list.append(i)
        # Answer to Task 4
        elif df.MA_20.iloc[i] < df.MA_50.iloc[i] and df.MA_20.iloc[i-1] > df.MA_50.iloc[i-1]:
            # Add the index of the sell signal to the Sell list
            sell_list.append(i)

    # now we can add the buy and sell signals to the dataframe
    # Add the buy signal to the dataframe
    df['Buy'] = df['Close'].iloc[buy_list]
    # Add the sell signal to the dataframe
    df['Sell'] = df['Close'].iloc[sell_list]
    print('\n')
    print(df.head(60))

    # Create a figure with 3 subplots and corresponding axes
    fig, axes = plt.subplots(nrows=3, ncols=1)
    print(fig)
    print(axes)
    fig.set_figheight(20)
    fig.set_figwidth(20)

    # Plot the data on the first subplot (axes[0]) in log scale
    # if you want it in true scale just delete the logy = True)
    df.plot(ax=axes[0], logy=True, grid=True)
    # Set the title and y-axis label
    axes[0].set(title="log Scale BTC Price & EMA",
                ylabel="United States Dollars")
    axes[0].yaxis.set_major_formatter(ScalarFormatter(
        useMathText=True))  # Set the y-axis to show dollars

    # plot buy and sell flags against the price on the second subplot (axes[1])
    # Plot the data on the second subplot
    df['Close'].plot(ax=axes[1], grid=True)
    df['Buy'].plot(ax=axes[1], logy=True, grid=True, marker='^', markersize=10,
                   color='green', linestyle='None')  # Plot the data on the first subplot
    df['Sell'].plot(ax=axes[1], logy=True, grid=True, marker='v', markersize=10,
                    color='red', linestyle='None')  # Plot the data on the first subplot
    # Set the title and y-axis label
    axes[1].set(title="Buy and Sell Flags", ylabel="United States Dollars")
    axes[1].yaxis.set_major_formatter(ScalarFormatter(
        useMathText=True))  # Set the y-axis to show dollars

    # plot the relative strengh axis
    # re-call this function since we deleted some NaN data after making the 50MA
    rsi_data = rsi(df, 14)
    rsi_data.plot(ax=axes[2], grid=True)
    ''' plot horizontal bars at y=70 and y=30'''
    # overbought value > 70 and oversold value < 30
    overBought = axes[2].axhline(
        y=70, linewidth=2, color='r', label='Overbought')
    overSold = axes[2].axhline(y=30, linewidth=2, color='g', label='Oversold')

    axes[2].legend(handles=[overBought, overSold])
    axes[2].set(title="Relative Strength Index")

    plt.show()  # Display the new graph

    holdings_in_cash = 1000  # $1000 starting cash
    # assume we bought in at the first price of BTC
    holdings_in_BTC = cash_to_BTC(holdings_in_cash, df['Close'].iloc[0])

    for i in range(len(df)):  # Loop through the df
        if i in buy_list:  # If the index is in the buy_list
            # convert all holdings in cash to BTC
            holdings_in_BTC = cash_to_BTC(
                holdings_in_cash, df['Close'].iloc[i])
            holdings_in_cash = 0
        elif i in sell_list:  # If the index is in the sell_list
            # Add the close price to the holdings
            holdings_in_cash = df['Close'].iloc[i] * holdings_in_BTC

    if holdings_in_cash == 0:  # If we still have holdings in BTC
        # Print the total holdings
        print("profit: ${:.2f}".format(holdings_in_cash - 1000))
    else:
        print("holdings in BTC: ${:.2f}".format(
            holdings_in_BTC))  # Print the total holdings
        # Print the total holdings cash value on last day of data
        print("current cash value: ${:.2f}".format(
            BTC_to_cash(holdings_in_BTC, df['Close'].iloc[i])))
        print("profit: ${:.2f}".format(BTC_to_cash(
            # Print the total holdings
            holdings_in_BTC, df['Close'].iloc[i]) - 1000))


if __name__ == "__main__":
    run()
