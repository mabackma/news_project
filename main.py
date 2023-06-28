import requests
from datetime import datetime
from config import NEWS_API_KEY

url = ('https://newsapi.org/v2/everything?'
       'q=conspiracy theory wagner&'
       'from=2023-06-26&'
       'sortBy=popularity&'
       f'apiKey={NEWS_API_KEY}')

response = requests.get(url)
response_json = response.json()

for item in response_json['articles']:
    print(f"{item['source']['name']} {datetime.strptime(item['publishedAt'], '%Y-%m-%dT%H:%M:%SZ').date()}:")
    print(item['title'])
    print(f"{item['url']}\n")
