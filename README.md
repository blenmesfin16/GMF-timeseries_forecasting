# Time Series Forecasting for Portfolio Management Optimization

## Project Overview
This project applies time series forecasting to historical financial data to enhance portfolio management strategies for GMF Investments.

### Assets Analyzed
- **TSLA** - High-growth stock (High risk, high potential return)
- **BND** - Vanguard Total Bond Market ETF (Low risk, stability)
- **SPY** - S&P 500 ETF (Moderate risk, broad market exposure)

### Time Period
January 1, 2015 - June 30, 2026

### Tasks
1. **Preprocess and Explore Data** - Data extraction, cleaning, EDA, stationarity testing
2. **Build Time Series Forecasting Models** - ARIMA/SARIMA + LSTM models
3. **Forecast Future Market Trends** - 6-12 month forecasts with confidence intervals
4. **Optimize Portfolio** - Efficient Frontier and Modern Portfolio Theory
5. **Strategy Backtesting** - Backtest vs. benchmark (60/40 SPY/BND)

### Installation
```bash
pip install -r requirements.txt