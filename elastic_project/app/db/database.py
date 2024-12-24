from elasticsearch import Elasticsearch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from elastic_project.app.settings.config import DB_URL

elastic_client = Elasticsearch(
   ['http://localhost:9200'],
   basic_auth=("elastic", "IRx0xI1y"),
   verify_certs=False
)


engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)