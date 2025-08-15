import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from NewsScraper import NewsScraper
from NewsArchive import NewsArchive
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

class StockPredictor: 
    def __init__(self, company_name): 
        self.ticker = None
        self.companies_data = {}
        self.company_dir = "archives"
        self.company_archive = os.path.join(self.company_dir, f"{company_name}_archive.json")
    
    def get_data(self, company_name):
        self.ticker = yf.Ticker(company_name)
        self.companies_data[company_name] = self.ticker
        
        return self.ticker.history(period='36mo')
    
    def predict_next_day(self, company_name):
        df = self.get_data(company_name)
        company_archive = NewsArchive.load_archives(self.company_archive)

        df['Target'] = df['Close'].shift(-1)
        df['Sentiment'] = 0
        df = df.dropna()
        df.index = pd.to_datetime(df.index).strftime('%Y-%m-%d')

        for date, articles in company_archive.items(): 
            sentiment = sum(article_entry["sentiment"] for article_entry in articles)

            if date in df.index: 
                df.loc[date, 'Sentiment'] = sentiment

        X = df[['Open', 'High', 'Low', 'Volume', 'Close', 'Sentiment']].values
        y = df['Target'].values

        model = LinearRegression()
        model.fit(X, y)


        last_row = df.iloc[-1][['Open', 'High', 'Low', 'Volume', 'Close', 'Sentiment']].values.reshape(1, -1)

        predicted_price = model.predict(last_row)[0]
        print(f"Predicted next trading day's close for {company_name}: {predicted_price:.2f}")
        print(df)
        
        return predicted_price

if __name__ == "__main__": 
    stocks = ["NVDA", "AAPL", "MSFT", "AMZN", "TSLA", "GOOGL", "META", "JNJ", "V", "JPM"] 
    for stock in stocks: 
        stock_predictor = StockPredictor(stock)
        stock_predictor.predict_next_day(stock) 


    