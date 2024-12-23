from flask import Flask, render_template

from app.routs.queries import terror_bluprint

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(terror_bluprint, url_prefix="/api/terror_data")
    app.run()