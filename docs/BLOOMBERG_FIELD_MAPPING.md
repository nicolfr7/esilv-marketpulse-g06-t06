# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

- Source: `data/sample/bloomberg_reference_sample.json`
- Reference: `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md` (not yet reviewed; mapping to be confirmed against it)
- Live connectivity: not demonstrated

The sample values are illustrative teaching values, not certified Bloomberg historical observations.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Inspected inputs

| Bloomberg identifier | Observations | Period | Missing values in observations |
|---|---|---|---|
| AAPL US Equity | 21 | 2026-09-01 to 2026-09-30 | None |
| SPX Index | 21 | 2026-09-01 to 2026-09-30 | None |

Both series have the same dates.

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | `observation_date` | `YYYY-MM-DD` string |
| ticker | application mapping from the series `canonical_ticker` | AAPL or SP500 |
| open | `open_value` | Numeric |
| high | `high_value` | Numeric |
| low | `low_value` | Numeric |
| close | `close_value` | Numeric |
| volume | `volume_value` | Numeric; 0 in all SPX Index observations |

These are teaching wrapper keys, not Bloomberg LIVE field mnemonics.

Teaching wrapper key != Bloomberg LIVE field mnemonic.

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: AAPL US Equity
- Benchmark identifier: SPX Index
- Date representation: `YYYY-MM-DD` string
- Input structure: root object > `series[]` (`role`, `canonical_ticker`, `provider_identifier`, `observations[]`)
- Missing fields: none in the observations. `ticker` is not repeated in each observation; it comes from the parent series.
- Special normalization notes:
  - Flatten both series into one list of canonical rows.
  - Rename the wrapper keys as shown in the field mapping.
  - Use `canonical_ticker` as `ticker`, never `provider_identifier`.
  - Keep a volume of 0 as 0; do not treat it as missing.
  - Do not create rows for dates absent from the sample.
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json` (42 rows under `rows`)