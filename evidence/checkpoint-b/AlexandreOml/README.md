# Checkpoint B

## Student

- Name: Alexandre Omiel
- GitHub: @AlexandreOml

## Contribution

- Branch: feature/yahoo-provider
- Main commits:
  - d1c5c37
  - bec2250
  - 798ced1
- Pull Request: #5 (+ #7 for the main.py provider switch)
- Reviewed Pull Request: #2

## Work completed

Implemented the Yahoo Finance provider (src/providers/yahoo_provider.py):
translation of canonical tickers to Yahoo symbols (SP500 -> ^GSPC) and
normalization of yfinance data into the canonical row contract
(date string, float prices, int volume, canonical ticker).
Added yfinance to requirements.txt and a PROVIDER switch in src/main.py
so MarketPulse runs on live Yahoo data or on the local CSV.
Applied the review feedback (notebook signature, auto_adjust=False).

## Main difficulty

Keeping the feature branch in sync with main while the analytics PR was
merged in parallel: divergent branches required a merge of main into
feature/yahoo-provider, and the provider switch had to go in a second PR
because PR #5 was merged before it was pushed.

## Evidence

- 01_pull_request.png
- 02_code_review.png
- 03_yahoo_market_data.png
- 04_instrument_benchmark.png