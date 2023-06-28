import requests
from datetime import datetime
from config import NEWS_API_KEY

def search(query: str,
           search_in: str = "title,description,content",
           sort_items: str = "publishedAt",
           language: str = "en",
           page_size: int = 100,
           page: int = 1,
           start: str = None,
           end: str = None):

    query = query
    search_in = search_in
    sort_by = sort_items  #relevancy, popularity, publishedAt
    language = language
    page_size = page_size  #100 is maximum
    page = page

    if start is not None:
        from_date = start
    else:
        from_date = datetime.now().date().strftime("%Y-%m-%d")
    if end is not None:
        to_date = end
    else:
        to_date = datetime.now().date().strftime("%Y-%m-%d")

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

search("conspiracy theory wagner", "title,description,content", "publishedAt", "en", 10, 1, "2023-06-25", "2023-06-26")
search("conspiracy theory wagner", start="2023-06-25", end="2023-06-26")