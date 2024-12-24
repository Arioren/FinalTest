from sqlalchemy import func
import pandas as pd
from first_half.app.db.database import session_maker
from first_half.app.db.model import Event, Casualties, AttackType, Region, Location

# 1
def deadliest_attack_types(filter_option="Top 5"):
    with session_maker() as session:
        query = (
            session.query(
                Event.attack_type_id,
                AttackType.name,
                func.sum(Casualties.killed * 2 + Casualties.wounded).label("score")
            )
            .join(Casualties)
            .join(AttackType, Event.attack_type_id == AttackType.id)
            .group_by(Event.attack_type_id, AttackType.name)
            .order_by(func.sum(Casualties.killed * 2 + Casualties.wounded).desc())
        )

        if filter_option == "Top 5":
            query = query.limit(5)

        result = query.all()

        return [{"name": row[1], "score": row[2]} for row in result]


# 2
def average_casualties_by_region(filter_option="Top 5"):
    with session_maker() as session:
        query = (
            session.query(
                Region.id,
                Region.name,
                func.avg(Location.latitude).label("latitude"),
                func.avg(Location.longitude).label("longitude"),
                func.avg(Casualties.killed * 2 + Casualties.wounded).label("average_casualties")
            )
            .join(Location, Region.id == Location.region_id)
            .join(Event, Location.id == Event.location_id)
            .join(Casualties)
            .group_by(Region.id, Region.name)
            .order_by(func.avg(Casualties.killed * 2 + Casualties.wounded).desc())
        )

        if filter_option == "Top 5":
            query = query.limit(5)

        result = query.all()

        return [
            {
                "region": row[1],
                "average_casualties": float(row[4]),
                "latitude": float(row[2]),
                "longitude": float(row[3]),
            }
            for row in result
        ]


# 8
def most_active_gangs_by_region(region_name=None):
    with session_maker() as session:
        query = (
            session.query(
                Region.name.label("region_name"),
                Event.gang_name.label("gang_name"),
                func.count(Event.id).label("event_count")
            )
            .join(Location, Event.location_id == Location.id)
            .join(Region, Location.region_id == Region.id)
            .group_by(Region.name, Event.gang_name)
            .order_by(func.count(Event.id).desc())
        )

        if region_name:
            query = query.filter(Region.name == region_name)

        result = query.all()

        data = {}
        for row in result:
            if row[1] is None or row[1] == "Unknown" or row[1] == "":
                continue
            region = row[0]
            gang = row[1]
            count = row[2]
            if region not in data:
                data[region] = []
            data[region].append({"gang_name": gang, "event_count": count})

        return data


# 6
def percentage_change_attacks_by_region(filter_option="Top 5"):
    with session_maker() as session:
        query = (
            session.query(
                Region.name.label("region_name"),
                Event.year.label("year"),
                func.count(Event.id).label("attack_count"),
                func.avg(Location.latitude).label("latitude"),
                func.avg(Location.longitude).label("longitude")
            )
            .join(Location, Event.location_id == Location.id)
            .join(Region, Location.region_id == Region.id)
            .group_by(Region.name, Event.year)
            .order_by(Region.name, Event.year)
        )

        result = query.all()

        df = pd.DataFrame(result, columns=["region_name", "year", "attack_count", "latitude", "longitude"])

        df["percentage_change"] = (
            df.groupby("region_name")["attack_count"]
            .pct_change() * 100
        )

        df = df.dropna()

        if filter_option == "Top 5":
            top_regions = df.groupby("region_name")["percentage_change"].max().nlargest(5).index
            df = df[df["region_name"].isin(top_regions)]

        return df

# 9
def correlation_between_terrorists_and_kills():
    with session_maker() as session:
        query = (
            session.query(
                Event.total_terrorists,
                func.avg(Casualties.killed).label("total_kills")
            )
            .join(Casualties, Event.casualties_id == Casualties.id)
            .group_by(Event.total_terrorists)
        )

        result = query.all()

        df = pd.DataFrame(result, columns=["total_terrorists", "total_kills"])

        correlation = df["total_terrorists"].corr(df["total_kills"])

        return correlation



