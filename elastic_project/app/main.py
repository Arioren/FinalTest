from flask import Flask

from elastic_project.app.routs.elastic_end_points import elastic_bluprint

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(elastic_bluprint, url_prefix="/api/elastic_data")
    app.run(host='0.0.0.0', port=5006)