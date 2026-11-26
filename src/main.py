from pathlib import Path
import csv
import json
import sys

# Permet les imports "src." avec : python src/main.py
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import src.analytics as analytics
from src.providers.yahoo_provider import CANONICAL_TO_YAHOO, fetch_yahoo_prices

DATA_DIR = Path("data/sample")

# "yahoo" for Yahoo Finance, "csv" for the local file
PROVIDER = "yahoo"

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def get_first_date(prices):
    return prices[0]["date"]


def get_last_date(prices):
    return prices[-1]["date"]


def main():
    instruments = load_instruments()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    if PROVIDER == "yahoo":
        instrument_prices = fetch_yahoo_prices(
            CANONICAL_TO_YAHOO[instrument["ticker"]], instrument["ticker"], "1mo", "1d"
        )
        benchmark_prices = fetch_yahoo_prices(
            CANONICAL_TO_YAHOO[benchmark["ticker"]], benchmark["ticker"], "1mo", "1d"
        )
    else:
        prices = load_prices()
        instrument_prices = filter_prices(prices, instrument["ticker"])
        benchmark_prices = filter_prices(prices, benchmark["ticker"])

    instrument_latest = instrument_prices[-1]
    benchmark_latest = benchmark_prices[-1]

    print("=== MarketPulse ===")
    print("Data source: Yahoo Finance" if PROVIDER == "yahoo" else "Data source: Local CSV")
    print()
    print("Instrument")
    print(f"{instrument['ticker']} - {instrument['name']}")
    print(f"Market: {instrument['market']}")
    print(f"{instrument['ticker']} price: {float(instrument_latest['close']):.2f} {instrument['currency']}")
    print(f"First observation: {get_first_date(instrument_prices)}")
    print(f"Last observation: {get_last_date(instrument_prices)}")
    print()
    print("Benchmark")
    print(f"{benchmark['ticker']} - {benchmark['name']}")
    print(f"Market: {benchmark['market']}")
    print(f"Last level: {float(benchmark_latest['close']):.2f}")
    print(f"First observation: {get_first_date(benchmark_prices)}")
    print(f"Last observation: {get_last_date(benchmark_prices)}")
    print()
    print(f"Period: {LOOKBACK_LABEL}")
    print(f"Interval: {INTERVAL_LABEL}")
    print()
    print("Observations")
    print(f"{instrument['ticker']}: {len(instrument_prices)}")
    print(f"{benchmark['ticker']}: {len(benchmark_prices)}")

    aligned_instrument, aligned_benchmark = analytics.align_series(
        instrument_prices, benchmark_prices
    )
    instrument_return = analytics.calculate_period_return(aligned_instrument)
    benchmark_return = analytics.calculate_period_return(aligned_benchmark)
    relative = analytics.calculate_relative_performance(
        instrument_return, benchmark_return
    )
    instrument_base = analytics.calculate_base_100(aligned_instrument)
    benchmark_base = analytics.calculate_base_100(aligned_benchmark)

    print()
    print("Performance")
    print(f"Common dates: {len(aligned_instrument)}")
    print(f"{instrument['ticker']} return: {instrument_return:+.2f}%")
    print(f"{benchmark['ticker']} return: {benchmark_return:+.2f}%")
    print(f"Relative performance: {relative:+.2f} pts")
    print(f"{instrument['ticker']} final base 100: {instrument_base[-1]['value']:.2f}")
    print(f"{benchmark['ticker']} final base 100: {benchmark_base[-1]['value']:.2f}")


if __name__ == "__main__":
    main()