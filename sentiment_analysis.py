import requests
import json

SENTIMENT_API_KEY = ''
SENTIMENT_API_URL = ''

def analyze_sentiment(headlines):
    sentiment_scores = []

    for headline in headlines:
        try:
            payload = {'text': headline, 'apiKey': SENTIMENT_API_KEY}
            response = requests.post(SENTIMENT_API_URL, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
            result = response.json()
            print(result)

            sentiment_score = result['sentiment_score']
            sentiment_scores.append(sentiment_score)

        except Exception as e:
            print(f"Error analyzing sentiment: {str(e)}")
            sentiment_scores.append(None)

    return sentiment_scores
