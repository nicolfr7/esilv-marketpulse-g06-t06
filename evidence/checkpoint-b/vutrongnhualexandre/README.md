# Checkpoint B — Collaboration and Data

## Étudiant

- Nom : Vu Trong Nhu Alexandre
- GitHub : @vutrongnhualexandre
- Groupe : G06
- Équipe : T06

## Contribution individuelle

- Branche : `feature/display-observation-dates`
- Commit principal : `a7ba4f6`
- Pull Request personnelle : #4
- Pull Requests examinées : #3 et #5
- Rôle TD08 : Étudiant 4 — Code Reviewer Yahoo Finance

## Travail réalisé

- Implémentation de l'affichage des premières et dernières dates d'observation.
- Création, publication et intégration d'une Pull Request.
- Analyse du module Yahoo Finance.
- Tests réels de récupération des données AAPL et SP500.
- Vérification de la normalisation des données et du tri chronologique.
- Demande de corrections et validation du module corrigé.
- Fusion de la Pull Request Yahoo Finance.
- Synchronisation de la branche main.

## Difficulté principale

Identification de deux différences entre le module Yahoo Finance et le notebook officiel TD08 :

- Signature non conforme de la fonction `fetch_yahoo_prices()`.
- Absence du paramètre `auto_adjust=False`.

Après correction par le développeur, les nouveaux tests ont permis de récupérer avec succès 23 observations pour chacun des deux actifs.

## Evidence

- 01_pull_request.png
- 02_code_review.png
- 03_yahoo_market_data.png
- 04_instrument_benchmark.png