"""MarketPulse Yahoo Finance provider (TD08).

Returns canonical observation rows, same shape as data/sample/prices.csv.
"""

import yfinance as yf

CANONICAL_TO_YAHOO = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


def fetch_yahoo_prices(
    symbol,
    canonical_ticker,
    period="1mo",
    interval="1d",
):
    """
    Retrieve historical market prices from Yahoo Finance and normalize to canonical format.

    Args:
        symbol (str): Yahoo Finance symbol (e.g., 'AAPL' or '^GSPC').
        canonical_ticker (str): Internal canonical ticker (e.g., 'AAPL' or 'SP500').
        period (str): Historical lookback window (default: '1mo').
        interval (str): Price frequency (default: '1d').

    Returns:
        list: Canonical observation dicts (date, ticker, open, high, low, close, volume),
        sorted by date ascending.
    """
    history = yf.Ticker(symbol).history(
        period=period,
        interval=interval,
        auto_adjust=False,
    )

    if history.empty:
        raise ValueError(
            f"No Yahoo Finance data returned for symbol {symbol} "
            f"(period={period}, interval={interval})."
        )

    rows = []
    for timestamp, row in history.iterrows():
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