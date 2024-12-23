import pandas as pd
import toolz as t
from sql_to_neo4j.app.db.database import session_maker, driver
from sql_to_neo4j.app.db.model import Event, Country, TargetType, AttackType, Region, Location


def from_sql_to_pd()->pd.DataFrame:
    with session_maker() as session:
        query = (
            session.query(
                Event.gang_name.label("gname"),
                Country.name.label("country_txt"),
                AttackType.name.label("attacktype1_txt"),
                TargetType.name.label("targtype1_txt"),
                Region.name.label("region_txt")
            )
            .join(Location, Event.location_id == Location.id)
            .join(Country, Location.country_id == Country.id)
            .join(Region, Location.region_id == Region.id)
            .join(AttackType, Event.attack_type_id == AttackType.id)
            .join(TargetType, Event.target_type_id == TargetType.id)
        )

        result = query.all()
        df = pd.DataFrame(result, columns=["gname", "country_txt", "attacktype1_txt", "targtype1_txt", "region_txt"])
        return df


def from_pd_to_dict(df):
    for index, row in df.iterrows():
        attack = {
            "country_name": row["country_txt"],
            "group_name": row["gname"],
            "type": row["attacktype1_txt"],
            "target": row["targtype1_txt"],
            "region_name": row["region_txt"]
        }
        from_dict_to_neo4j(attack)


def from_dict_to_neo4j(attack):
    with driver.session() as session:
        query = """
        merge(r: Region{name:$region_name})
        merge(c: Country{name:$country_name})
        merge(g: Group{name:$group_name})
        merge(g) - [:ATTACKED{type:$type,
                target:$target}]-> (c)
        merge (c) -[:IS_IN]-> (r)
        return c, g,r
        """
        params = {
            "country_name": attack['country_name'],
            "group_name": attack['group_name'],
            "type": attack['type'],
            "target": attack['target'],
            "region_name": attack['region_name']
        }
        res = session.run(query, params).data()
        return t.pipe(
            res,
            t.partial(t.pluck, 'c'),
            list
        )


def insert_to_neo4j():
    df = from_sql_to_pd()
    from_pd_to_dict(df)