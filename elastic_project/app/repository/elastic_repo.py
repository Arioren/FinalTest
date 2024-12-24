from elastic_project.app.db.database import elastic_client


def search(keyword, start_date=None, end_date=None, source=None):
    must_clauses = []

    if keyword:
        must_clauses.append({"match": {"description": keyword}})

    if start_date and end_date:
        must_clauses.append({
            "range": {
                "date": {
                    "gte": start_date,
                    "lte": end_date,
                    "format": "yyyy-MM-dd"
                }
            }
        })

    if source:
        must_clauses.append({"term": {"source": source}})

    search_query = {
        "query": {
            "bool": {
                "must": must_clauses
            }
        }
    }

    response = elastic_client.search(index="terror_data", body=search_query)

    return response