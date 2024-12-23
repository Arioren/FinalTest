from neo4j import GraphDatabase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings.config import DB_URL
from sql_to_neo4j.app.settings.neo4j import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)


driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)