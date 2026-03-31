from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests 

def fetch(url):
    headers = {"User-Agent":"NeeSEnti"}
    response = requests.get(url, headers=headers)
    return response.json()['data']['children']

world_news_posts = fetch("https://www.reddit.com/r/worldnews/.json?limit=50")
wsb_posts = fetch("https://www.reddit.com/r/wallstreetbets/.json?limit=50")

all_posts = world_news_posts + wsb_posts

analyzer = SentimentIntensityAnalyzer()
all_titles = ""
final_scores = []

for post in all_posts:
    title = post['data']['title']
    all_titles += " " + title  
    score = analyzer.polarity_scores(title)['compound']
    final_scores.append(score)

avg_sentiment = sum(final_scores) / len(final_scores)

wsb = ""
wsb_score = []
for bets in wsb_posts:
	t = bets["data"]["title"]
	wsb+=(t)
	wscore = analyzer.polarity_scores(t)['compound']
	wsb_score.append(wscore)

wn = ""
wn_score = []
for news in world_news_posts:
	n = news["data"]["title"]
	wn+=(n)
	wnscore = analyzer.polarity_scores(n)['compound']
	wn_score.append(wnscore)
wncore = analyzer.polarity_scores(wn)
avg_wn = sum(wn_score) / len(wn_score)
print("r/worldnews' compounded score is(representing world news)",avg_wn)
print("r/worldnews negative index", "=", wncore["neg"])
print("r/worldnews neutral index", "=", wncore["neu"])
print("r/worldnews positive index", "=", wncore["pos"])

wscore = analyzer.polarity_scores(wsb)
avg_wsb = sum(wsb_score) / len(wsb_score)
print("r/wallstreetbets' compounded score is(representing public's sentiments)",avg_wsb)
print("r/wallstreetbets negative index", "=", wscore["neg"])
print("r/wallstreetbets neutral index", "=", wscore["neu"])
print("r/wallstreetbets positive index", "=", wscore["pos"])

print(f"Combined (WorldNews + WSB) Sentiment Score: {avg_sentiment}")
score = analyzer.polarity_scores(all_titles)
print("overall negative index", "=", score["neg"])
print("overall neutral index", "=", score["neu"])
print("overall positive index", "=", score["pos"])
weighted_sentiment = (avg_wn*35 + avg_wsb*65)/100
print("weighted sentiment where news is weighted 35% and public sentiment is weighted 65% ,weighted_sentiment = ",weighted_sentiment)
divergence = abs(avg_wn - avg_wsb)
print("divergence in news and people (if d<0.15 then it's stable and d>0.3 then it's stressed) = ",divergence)
