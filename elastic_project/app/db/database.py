from elasticsearch import Elasticsearch

elastic_client = Elasticsearch(
   ['http://localhost:9200'],
   basic_auth=("elastic", "IRx0xI1y"),
   verify_certs=False
)
