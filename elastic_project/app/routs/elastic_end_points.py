from flask import Blueprint, request, jsonify

from elastic_project.app.repository.elastic_repo import search

elastic_bluprint = Blueprint('elastic_bluprint', __name__)

# חיפוש בכל מקורות הנתונים
@elastic_bluprint.route('/search/keywords', methods=['POST'])
def keywords_search():
    try:
        data = request.json
        keyword = data.get('keyword')
        res = search(keyword=keyword)
        return jsonify(res)
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# חיפוש בנתוני חדשות בזמן אמת
@elastic_bluprint.route('/search/news', methods=['GET'])
def news_search():
    try:
        data = request.json
        keyword = data.get('keyword')
        res = search(keyword=keyword, source="news")
        return jsonify(res)
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
# חיפוש בנתונים ההיסטוריים
@elastic_bluprint.route('/search/historic', methods=['GET'])
def historic_search():
    try:
        data = request.json
        keyword = data.get('keyword')
        res = search(keyword=keyword, source="historic")
        return jsonify(res)
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@elastic_bluprint.route('/search/combined', methods=['GET'])
def combined_search():
    try:
        data = request.json
        keyword = data.get('keyword')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        res = search(keyword=keyword, start_date=start_date, end_date=end_date)
        return jsonify(res)
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500