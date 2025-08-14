import yfinance as yf
import json
import os
from datetime import datetime 

class NewsArchive: 
    def __init__(self):
        pass
        
    @staticmethod
    def load_archives(file_name): 
        try: 
            if os.path.getsize(file_name) == 0:
                return {}
            with open(file_name, 'r') as file: 
                return json.load(file)
        except FileNotFoundError: 
            return {}

    @staticmethod
    def save_archive(file_name, archive): 
        try: 
            with open(file_name, 'w') as file: 
                json.dump(archive, file, indent=2)
        except FileNotFoundError: 
            return []

    @staticmethod
    def load_seen_urls(url_file): 
        try: 
            if os.path.getsize(url_file) == 0:
                return set()
            with open(url_file, 'r') as file: 
                return set(json.load(file))
        except FileNotFoundError: 
            return set()
        
    @staticmethod
    def save_seen_urls(url_file, seen_urls): 
        try: 
            with open(url_file, 'w') as file: 
                json.dump(list(seen_urls), file, indent=2)
        except FileNotFoundError: 
            return []
        
    @staticmethod
    def add_article(company_archive, title, url, date, sentiment_score):
        if date is None: 
            date = datetime.now().strftime("%Y-%m-%d")

        article_entry = {
            "title": title,
            "date": date,  
            "url": url,
            "sentiment": sentiment_score
        } 

        if date not in company_archive: 
            company_archive[date] = []
        
        company_archive[date].append(article_entry)

    