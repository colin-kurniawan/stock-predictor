import yfinance as yf
import requests
import json
import os 
from newspaper import Article
from bs4 import BeautifulSoup
from NewsArchive import NewsArchive

class NewsScraper: 
    def __init__(self, company_name): 
        self.archive_dir = "archives"
        self.file_name = os.path.join(self.archive_dir, f"{company_name}_archive.json")
        self.url_file = os.path.join(self.archive_dir, f"{company_name}_seen_urls.json")
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.articles = set()
        self.seen_urls = NewsArchive.load_seen_urls(self.url_file)
        self.company_archive = NewsArchive.load_archives(self.file_name)
        self.ticker_to_name = {
            "AAPL": "apple",
            "AMZN": "amazon",
            "GOOGL": "google",
            "JNJ": "johnson",
            "JPM": "morgan",
            "META": "meta",
            "MSFT": "microsoft",
            "NVDA": "nvidia",
            "TSLA": "tesla",
            "V": "visa"
        }

    def get_data(self, company_name): 
        data = yf.Search(company_name, news_count=1000)

        data.search()

        for news_article in data.news: 
            url = news_article["link"]
            title = news_article["title"]

            if company_name in url or self.ticker_to_name[company_name] in url:
                if url in self.seen_urls: 
                    continue
                else: 
                    date = self.get_date(url)
                    sentiment_score = self.analyze_article(url)
                    self.seen_urls.add(url) 
                    NewsArchive.add_article(self.company_archive, title, url, date, sentiment_score)
            else: 
                continue

        NewsArchive.save_seen_urls(self.url_file, self.seen_urls)
        NewsArchive.save_archive(self.file_name, self.company_archive)

    def analyze_article(self, url): 
        positive_indicators = {"growth", "profit", "increase", "surge", "strong", "upgrade", "buy", "bullish"}
        negative_indicators = {"loss", "decline", "missed", "downgrade", "weak", "cut", "sell", "bearish", "lawsuit", "scandal"}
        sentiment = 0

        article = self.analyze_article_aux(url)
        words = article.split()
        
        for word in words: 
            if word.lower() in positive_indicators: 
                sentiment += 1
            elif word.lower() in negative_indicators: 
                sentiment -= 1
            else: 
                continue

        return sentiment

    def analyze_article_aux(self, url): 
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200: 
            article = Article(url)
            article.set_html(response.text)
            article.parse()
            return article.text

    def get_date(self, url): 
        response = requests.get(url, headers=self.headers)
                
        soup = BeautifulSoup(response.text, 'html.parser')

        for time_tag in soup.find_all("time"): 
            full_date = time_tag.get("datetime")
            year_month_day = full_date.split("T")[0]
        return year_month_day
                   
if __name__ == "__main__":
    stocks = ["NVDA", "AAPL", "MSFT", "AMZN", "TSLA", "GOOGL", "META", "JNJ", "V", "JPM"]  
    for stock in stocks: 
        news_scraper = NewsScraper(stock)
        news_scraper.get_data(stock) 

    

