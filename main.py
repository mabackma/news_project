import requests
from datetime import datetime
from config import NEWS_API_KEY

def search(query: str, search_in: str, from_date: str, to_date: str, sort_by: str, language: str, page_size: int, page: int):
    query = query
    search_in = search_in
    from_date = from_date
    to_date = to_date
    sort_by = sort_by  #relevancy, popularity, publishedAt
    language = language
    page_size = page_size  #100 is maximum
    page = page

    url = ('https://newsapi.org/v2/everything?'
           f'q={query}&'
           f'searchIn={search_in}&'
           f'from={from_date}&'
           f'to={to_date}&'
           f'language={language}&'
           f'sortBy={sort_by}&'
           f'pageSize={page_size}&'
           f'page={page}&'
           f'apiKey={NEWS_API_KEY}')

    response = requests.get(url)
    response_json = response.json()

    for item in response_json['articles']:
        print(f"{item['source']['name']} {datetime.strptime(item['publishedAt'], '%Y-%m-%dT%H:%M:%SZ').date()}:")
        print(item['title'])
        print(f"{item['url']}\n")

search("conspiracy theory wagner", "title,description,content", "2023-06-25", "2023-06-26", "publishedAt", "en", 10, 1)