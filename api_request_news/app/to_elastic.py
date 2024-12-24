from elasticsearch.helpers import bulk

from api_request_news.app.db.database import elastic_client


def insert_to_elasticsearch(data):
    elastic_client.index(index="terror_data", body=data)


def init_elastic():
    if elastic_client.indices.exists(index="terror_data"):
        elastic_client.indices.delete(index="terror_data")

    elastic_client.indices.create(index="terror_data", body={
       "settings": {
           "number_of_shards": 2,
           "number_of_replicas": 2
       },
       "mappings": {
        "properties": {
            "latitude": {"type": "geo_point"},
            "longitude": {"type": "geo_point"},
            "date": {
                "type": "date",
                "format": "yyyy-MM-dd"
            },
            "description": {
                "type": "text",
                "analyzer": "standard"
            },
            "country": {"type": "keyword"},
            "city": {"type": "keyword"},
            "type": {"type": "keyword"},
            "source": {"type": "keyword"}
        }
       }
    })