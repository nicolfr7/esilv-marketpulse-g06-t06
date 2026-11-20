from pathlib import Path
import csv
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.providers.yahoo_provider import CANONICAL_TO_YAHOO, fetch_yahoo_prices


DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"
PROVIDER = "yahoo"   # "csv" pour revenir aux fichiers locaux


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
    print(f"{instrument['ticker']} price: {instrument_latest['close']} {instrument['currency']}")
    print(f"First observation: {get_first_date(instrument_prices)}")
    print(f"Last observation: {get_last_date(instrument_prices)}")
    print()
    print("Benchmark")
    print(f"{benchmark['ticker']} - {benchmark['name']}")
    print(f"Market: {benchmark['market']}")
    print(f"Last level: {benchmark_latest['close']}")
    print(f"First observation: {get_first_date(benchmark_prices)}")
    print(f"Last observation: {get_last_date(benchmark_prices)}")
    print()
    print(f"Period: {LOOKBACK_LABEL}")
    print(f"Interval: {INTERVAL_LABEL}")
    print()
    print("Observations")
    print(f"{instrument['ticker']}: {len(instrument_prices)}")
    print(f"{benchmark['ticker']}: {len(benchmark_prices)}")
    print(f"Market:{instrument['market']}")
    print(f"Market: {benchmark['market']}")


if __name__ == "__main__":
    main()