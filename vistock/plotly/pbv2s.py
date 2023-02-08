"""
Visualize a PBV (means price-by-volume, also called volume profile) for a given
stock. Here the PBV is overlaid with the price subplot (total 2 subplots).
"""
__software__ = "Volume Profile 2-split with Plotly"
__version__ = "1.01"
__author__ = "York <york.jong@gmail.com>"
__date__ = "2023/02/06 (initial version) ~ 2023/02/07 (last revision)"

import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots


def show_pbv2s_plotly(ticker='TSLA', period='12mo', total_bins=42):
    """Visualize a PBV (means price-by-volume, also called volume profile) for a
    given stock. Here the PBV overlaied with the price subplot. This figure
    consists of two subplots: a price subplot and a volume subplot. The former
    includes candlestick, moving average lines, while the latter includes
    trading volume bar chart and volume moving average line.

    Parameters
    ----------
    ticker
        the ticker name (default is 'TSLA')
    period
        the period (default is '12mo' that means 12 monthes)
    total_bins
        the number of bins to calculate comulative volume for bins.
    """
    # Download stock data
    df = yf.Ticker(ticker).history(period=period)

    # Initialize empty plot with a marginal subplot
    fig = make_subplots(
        rows=2, cols=1,
        row_heights=[0.7, 0.3],
        #shared_xaxes=True,
        vertical_spacing=0.03,
        specs=[
            [{"secondary_y": True}],    # row 1, col 1
            [{"secondary_y": False}]    # row 2, col 1
        ],
        figure=go.Figure(layout=go.Layout(height=720))
    )
    #print(fig)

    # Plot the candlestick chart
    candlestick = go.Candlestick(
        x=df.index,
        open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'],
        name='OHLC',
        xaxis='x2', yaxis='y2',
    )
    fig.add_trace(candlestick)

    # Add moving averages to the figure
    ma_days = (5, 10, 20, 50, 150)
    ma_colors = ('orange', 'red', 'green', 'blue', 'brown')
    for d, c in zip(ma_days, ma_colors):
        df[f'ma{d}'] = df['Close'].rolling(window=d).mean()
        ma = go.Scatter(
            x=df.index, y=df[f'ma{d}'], name=f'MA {d}',
            line=dict(color=f'{c}', width=2),
            xaxis='x2', yaxis='y2',
        )
        fig.add_trace(ma)

    # Add Price by Volume (Volume Profile) chart
    bin_size = (max(df['High']) - min(df['Low'])) / total_bins
    bin_round = lambda x: bin_size * round(x / bin_size)
    bin = df['Volume'].groupby(df['Close'].apply(lambda x: bin_round(x))).sum()
    vp = go.Bar(
        y=bin.keys(),   # Price
        x=bin.values,   # Bin Comulative Volume
        text=bin,       # (price, volume) pairs
        name="Price Bins",
        orientation="h",    # 'v', 'h'
        marker_color="brown",
        texttemplate="%{x/1000:3.2fK}",
        hoverinfo="y",   # 'x', 'y', 'x+y'
        opacity=0.3,
        xaxis='x', yaxis='y',
    )
    fig.add_trace(vp)

    # Add volume trace to 2nd row
    colors = ['green' if o - c >= 0
            else 'red' for o, c in zip(df['Open'], df['Close'])]
    volume = go.Bar(
        x=df.index, y=df['Volume'], name='Volume',
        marker_color=colors, opacity=0.7,
        #xaxis='x2', yaxis='y3',
    )
    fig.add_trace(volume, row=2, col=1)

    # Add moving average volume to 2nd row
    df['vma50'] = df['Volume'].rolling(window=50).mean()
    vma50 = go.Scatter(x=df.index, y=df['vma50'], name='VMA 50',
                    line=dict(color='purple', width=2),
                    #xaxis='x2', yaxis='y3'
            )
    fig.add_trace(vma50, row=2, col=1)

    # Remove non-trading dates
    df.index = df.index.strftime('%Y-%m-%d')
    dt_all = pd.date_range(start=df.index.values[0], end=df.index.values[-1])
    dt_all = [d.strftime("%Y-%m-%d") for d in dt_all]
    trade_date = [d for d in df.index.values]
    dt_breaks = list(set(dt_all) - set(trade_date))
    fig.update_xaxes(rangebreaks=[dict(values=dt_breaks)])

    # Update layout
    fig.update_layout(
        title=f'{ticker}: {df.index.values[0]}~{df.index.values[-1]}',
        title_x=0.5, title_y=.98,

        xaxis=dict(side='top', title='Bin Comulative Volume'),
        yaxis=dict(side='left', title='Bin Price (USD)'),

        xaxis2=dict(overlaying='x', side='bottom', title='Date'),
        yaxis2=dict(side='right', title='Price (USD)'),
        yaxis3=dict(side='right', title='Volume'),

        legend=dict(yanchor='middle', y=0.5, xanchor="left", x=0.01),
        xaxis_rangeslider_visible=False,
        xaxis2_rangeslider_visible=False,
    )

    # Add crosshair cursor
    fig.update_yaxes(
        spikemode='across', spikesnap='cursor',
        spikethickness=1, spikedash='solid', spikecolor='grey')
    fig.update_xaxes(
        spikemode='across', spikesnap='cursor',
        spikethickness=1, spikedash='solid', spikecolor='grey')
    fig.update_layout(hovermode='x')  # 'x', 'y', 'closest', False, 'x unified',
                                      # 'y unified'

    # Show the figure
    fig.show()


if __name__ == '__main__':
    ticker = "TSLA" #@param {type:"string"}
    period = "12mo" #@param ["3mo", "6mo", "12mo", "24mo"]
    total_bins = 42 #@param {type: "integer"}
    show_pbv2s_plotly(ticker=ticker, period=period, total_bins=total_bins)
