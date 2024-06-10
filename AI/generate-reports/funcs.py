import yfinance as yf
import requests
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import datetime
print(datetime.datetime.today())

text ="ban"
print(text.split("a"))
# Set API keys
NEWSAPI_API_KEY = ''

# Fetch historical cryptocurrency prices using yfinance (or another API)
def fetch_crypto_data(crypto_symbol):
    crypto = yf.Ticker(crypto_symbol)
    crypto_history = crypto.history()
    return crypto_history

# Fetch recent news using NewsAPI
def fetch_news(crypto_symbol, api_key):
    NEWSAPI_URL = "https://newsapi.org/v2/everything"
    params = {
        "q": crypto_symbol,
        "sortBy": "publishedAt and relevancy",
        "apiKey": api_key
    }
    #         "searchIn": "description",
    response = requests.get(NEWSAPI_URL, params=params)
    news_data = response.json()
    return news_data

# Perform sentiment analysis on news articles
def analyze_sentiment(news_data):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []
    for article in news_data['articles']:
        text = article['title'] + " " + article['description']
        score = analyzer.polarity_scores(text)
        sentiments.append(score)
    average_sentiment = pd.DataFrame(sentiments).mean()
    return average_sentiment

data = yf.download("BTC-USD")
data = pd.DataFrame(data)
print(data.tail(750))
'''crypto_symbol = 'BTC-USD'
crypto_name = 'Bitcoin'
data = fetch_crypto_data(crypto_symbol)
news_data = fetch_news(crypto_name, NEWSAPI_API_KEY)
print(len(news_data))
sentiment = analyze_sentiment(news_data)
print(sentiment)'''
