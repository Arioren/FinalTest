from elastic_project.app.db.database import elastic_client
from datetime import datetime

def search(keyword, start_date:str=None, end_date:str=None, source=None):
    must_clauses = []

    if keyword:
        must_clauses.append({"match": {"description": keyword}})

    if source:
        must_clauses.append({"term": {"source": source}})

    search_query = {
        "query": {
            "bool": {
                "must": must_clauses
            }
        }
    }

    response = elastic_client.search(index="terror_data", body=search_query)["hits"]["hits"]

    if start_date and end_date:
        final_response = []
        for res in response:
            try:
                if (datetime.strptime(start_date, "%Y-%m-%d") <=
                    datetime.strptime(res["_source"]["date"], "%Y-%m-%d") <=
                    datetime.strptime(end_date, "%Y-%m-%d")):
                    final_response.append(res)
            except:
                continue

        return final_response

    return response