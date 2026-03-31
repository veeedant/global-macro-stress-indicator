import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentEngine:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.headers = {"User-Agent": "python:macro_stress_project:v1.0 (by /u/VedantArora_DU)"}

    def fetch_reddit(self, subreddit):
        url = f"https://www.reddit.com/r/{subreddit}/.json?limit=50"
        try:
            response = requests.get(url, headers=self.headers)
            return response.json()['data']['children']
        except:
            return []

    def get_scores(self):
        # Fetching
        world_news = self.fetch_reddit("worldnews")
        wsb = self.fetch_reddit("wallstreetbets")

        # Scoring Logic
        wn_scores = [self.analyzer.polarity_scores(p['data']['title'])['compound'] for p in world_news]
        wsb_scores = [self.analyzer.polarity_scores(p['data']['title'])['compound'] for p in wsb]

        avg_wn = sum(wn_scores) / len(wn_scores) if wn_scores else 0
        avg_wsb = sum(wsb_scores) / len(wsb_scores) if wsb_scores else 0

        # Calculations
        weighted_sentiment = (avg_wn * 35 + avg_wsb * 65) / 100
        divergence = abs(avg_wn - avg_wsb)

        return {
            "avg_wn": avg_wn,
            "avg_wsb": avg_wsb,
            "weighted_sentiment": weighted_sentiment,
            "divergence": divergence
        }
