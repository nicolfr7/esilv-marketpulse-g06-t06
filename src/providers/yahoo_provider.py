"""MarketPulse Yahoo Finance provider (TD08).

Returns canonical observation rows, same shape as data/sample/prices.csv.
"""

import yfinance as yf

CANONICAL_TO_YAHOO = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


def fetch_yahoo_prices(canonical_ticker, lookback="1mo", interval="1d"):
    if canonical_ticker not in CANONICAL_TO_YAHOO:
        raise ValueError(f"Unknown ticker: {canonical_ticker}")

    yahoo_symbol = CANONICAL_TO_YAHOO[canonical_ticker]
    raw = yf.Ticker(yahoo_symbol).history(period=lookback, interval=interval)

    if raw.empty:
        raise ValueError(f"No data returned by Yahoo for {yahoo_symbol}")

    rows = []
    for timestamp, row in raw.iterrows():
        rows.append(
            {
                "date": timestamp.strftime("%Y-%m-%d"),
                "ticker": canonical_ticker,
                "open": float(row["Open"]),
                "high": float(row["High"]),
                "low": float(row["Low"]),
                "close": float(row["Close"]),
                "volume": int(row["Volume"]),
            }
        )

    rows.sort(key=lambda r: r["date"])
    return rows