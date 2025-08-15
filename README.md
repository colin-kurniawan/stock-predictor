# Stock Predictor

A Python-based stock prediction tool that forecasts stock prices for Nvidia, Apple, Microsoft, Amazon, Tesla, Google, Meta, Johnson & Johnson, Visa, and JP Morgan using historical data and public sentiment. This project combines data fetching, web scraping, preprocessing, and machine learning to provide actionable insights into stock trends.

## Features

- **JSON Database for Sentiment Tracking** – Maintain a structured JSON database storing sentiment scores, article URLs, and relevant metadata for each company. This allows for easy updates and historical tracking of public sentiment.
- **Historical Stock Data Fetching** – Pull stock price data for mentioned companies using `yfinance`.
- **Web Scraping for Sentiment Analysis** – Analyze news articles and public content to extract sentiment scores for each stock.
- **Data Preprocessing** – Combine stock prices and sentiment scores into a clean dataset for modeling.
- **Machine Learning Predictions** – Uses Linear Regression to predict future stock prices based on both historical data and sentiment metrics.

## Technologies Used

- Python 3.x
- `yfinance` for financial data
- `pandas` and `numpy` for data processing
- `scikit-learn` for machine learning models
- `matplotlib` for visualization
- `BeautifulSoup` or `requests` for web scraping sentiment data

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/colin-kurniawan/stock_predictor.git
2. Then in the terminal run:
   ```bash
   cd stock-predictor
   ```
   ```bash
   code .
   ```
3. Activate the virtual environemnt:
   ```bash
   source .venv/bin/activate
   ```
## Usage 

- To predict the stock prices for the 10 companies listed above, run:
  ```bash
  python3 StockPredictor.py
  ```
- To pull websites from yfinance and store into their respective archive files, run:
  ```bash
  python3 NewsScraper.py
  ```

## Planned Features

- **Advanced Machine Learning Models** – Explore and implement models such as Random Forests, Gradient Boosting, LSTM, and ARIMA to improve prediction accuracy beyond Linear Regression.  
- **Full S&P 500 Coverage** – Expand the system to predict stock prices for all companies in the S&P 500, allowing for broader market analysis and portfolio-level insights.  
