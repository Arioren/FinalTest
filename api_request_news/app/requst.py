import requests

from api_request_news.app.groq_request import get_type_of_event, get_city_and_country
from api_request_news.app.to_elastic import init_elastic, insert_to_elasticsearch

api_key = "bafb3aaa-7c30-4992-b209-f2b47fd6b21a"


def get_news_data():
    url = f"https://eventregistry.org/api/v1/article/getArticles"
    params = {
        "action": "getArticles",
        "keyword": "terror attack",
        "ignoreSourceGroupUri": "paywall/paywalled_sources",
        "articlesPage": 1,
        "articlesCount": 100,
        "articlesSortBy": "socialScore",
        "articlesSortByAsc": False,
        "dataType": [
        "news",
        "pr"
        ],
        "forceMaxDataTimeWindow": 31,
        "resultType": "articles",
        "apiKey": api_key
        }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}




def search_type(data):
    res = []
    data = data["articles"]
    data = data["results"]
    for item in data:
        news_type = get_type_of_event(item['body']).lower()
        if news_type == "terrorism" or news_type == "historical" or news_type == "current":
            item['type'] = news_type
            res.append(item)
        else:
            continue
    return res


def search_city_and_country(item):
    try:
        city, country, lat, lon = get_city_and_country(item['body']).split(", ")
    except Exception as e:
        city, country, lat, lon = "Unknown", "Unknown", "Unknown", "Unknown"
    item['city'] = city
    item['country'] = country
    item['latitude'] = lat
    item['longitude'] = lon


if __name__ == '__main__':
    init_elastic()
    array = []
    data = get_news_data()
    only_terrorism_history_current = search_type(data)
    for item in only_terrorism_history_current:
        search_city_and_country(item)
        array.append({
        "date": item["date"],
        "description": item["body"],
        "country": item["country"],
        "city": item["city"],
        "type": item["type"],
        "source": 'news',
        "latitude": item["latitude"],
        "longitude": item["longitude"]
    })
    insert_to_elasticsearch(array)


