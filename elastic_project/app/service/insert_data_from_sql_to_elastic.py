from elastic_project.app.db.database import session_maker, elastic_client
from elastic_project.app.db.model import Event, Location, Country, City



def insert_data_from_sql_to_elastic():
    with session_maker() as session:
        query = (
            session.query(
                Event.year,
                Event.month,
                Event.day,
                Location.latitude,
                Location.longitude,
                Country.name,
                City.name,
                Event.description
            )
            .join(Location, Event.location_id == Location.id)
            .join(Country, Location.country_id == Country.id)
            .join(City, Location.city_id == City.id)
        )

        result = query.all()
        # insert result to elastic
        for row in result:
            data = {
                'date': f'{row[0]}-{row[1]}-{row[2]}',
                "description": row[7],
                "country": row[5],
                "city": row[6],
                "type": "terrorism",
                "source": 'history',
                "latitude": row[3],
                "longitude": row[4]
            }

            insert_elastic(data)

def insert_elastic(data):
    elastic_client.index(index="terrorism", body=data)
