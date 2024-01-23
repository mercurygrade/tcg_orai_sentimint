from newsapi import NewsApiClient
import requests

api_key = "api-key"
newsapi = NewsApiClient(api_key=api_key)
queires = ["bitcoin", "ethereum", "dogecoin", "cryptocurrency"]
for query in queires:  
    cyrpto_news = newsapi.get_everything(
        q=query,
    )
    for article in cyrpto_news["articles"]:
        try:
            text = article["content"]
        except AttributeError:
            print("AttributeError: 'NoneType' object has no attribute 'content'")
        
        if text:
           
            api_url = 'https://api.api-ninjas.com/v1/sentiment?text={}'.format(text)
            try:
                response = requests.get(api_url, headers={'X-Api-Key': 'api-key'})
                response.raise_for_status()  

                data = response.json()

                print(data)
            except requests.exceptions.RequestException as e:
                print("Error:", e)
