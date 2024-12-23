from flask import Flask

from neo4j_queries.app.routs.all_routs import neo4j_queries_bluprint

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(neo4j_queries_bluprint, url_prefix="/api/terror_data/neo4j")
    app.run()