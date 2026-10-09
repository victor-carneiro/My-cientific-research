# Modeling BRL/USD Exchange Rate Dynamics with Geometric Brownian Motion

Undergraduate research project at PUC-Rio (January – August 2026), selected
for the Best Undergraduate Research contest in Rio de Janeiro.

## Overview
This project models BRL/USD exchange rate fluctuations using Geometric
Brownian Motion (GBM) with drift. The analysis tests whether log-returns
behave as a random walk with a consistent trend component and volatility
that scales with the square root of time.

## Methodology
- Processed historical BRL/USD exchange rate data
- Computed log-returns and tested whether they are approximately normally distributed
- Estimated drift and volatility parameters
- Checked the stability of these parameters across different sampling intervals
- Validated the GBM model against the historical data

## Applications
The results support the use of GBM in derivatives pricing and currency risk
management.

## Tools
Python (pandas, numpy, matplotlib)

## Repository Structure
- `data/`: historical exchange rate data
- `notebooks/`: exploratory analysis and validation
- `src/`: parameter estimation and statistical tests
- `report/`: written research report

## How to Run
pip install -r requirements.txt
python src/main.py

## Author
Victor de Castro Carneiro
Industrial Engineering, PUC-Rio | Exchange student at UC Berkeley
[LinkedIn](https://linkedin.com/in/victor-carneiro-89523a272)
