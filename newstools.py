import requests
from datetime import datetime, timedelta
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

    # Make the request to newsapi.org
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

    return get_response(url)


def top_headlines(country: str, category: str):

    # Make the request to newsapi.org
    url = ('https://newsapi.org/v2/top-headlines?'
           f'country={country}&'
           f'category={category}&'
           f'apiKey={NEWS_API_KEY}')

    return get_response(url)


def get_response(url: str):
    response = requests.get(url)
    response_json = response.json()

    news_count = response_json["totalResults"]

    # Make a list of news dictionaries from the response
    all_news = []
    for item in response_json['articles']:
        publisher = item['source']['name']
        published_at = datetime.strptime(item['publishedAt'], '%Y-%m-%dT%H:%M:%SZ').date()
        title = item['title']
        news_url = item['url']
        news_image = item['urlToImage']

        news = {"publisher": publisher, "published_at": published_at, "title": title, "news_url": news_url, "news_image": news_image}
        all_news.append(news)

    # Return the list of news dictionaries.
    return (news_count, all_news)