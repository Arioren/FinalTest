from app.db.database import session_maker, engine
from app.db.model import TargetType, AttackType, Country, Region, City, Location, Casualties, Event, Base
import csv


def read_csv_data(file_path):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    target_cache = {}
    attack_cache = {}
    region_cache = {}
    country_cache = {}
    city_cache = {}
    location_cache = {}

    with open(file_path, 'r', encoding='iso-8859-1') as file:
        reader = csv.reader(file)
        next(reader)

        events = []

        with session_maker() as session:
            for i, line in enumerate(reader):
                target_name = line[35]
                attack_name = line[29]
                region_name = line[10]
                country_name = line[8]
                city_name = line[12]
                latitude = float(line[13]) if line[13] else None
                longitude = float(line[14]) if line[14] else None
                killed = int(float(line[98])) if line[98] and int(float(line[98])) >= 0 else None
                wounded = int(float(line[99])) if line[99] and int(float(line[99])) >= 0 else None
                year, month, day = line[1], line[2], line[3]
                gang_name = line[58]
                total_terrorists = int(float(line[69])) if line[69] and int(float(line[69])) >= 0 else None
                description = line[18]

                if target_name not in target_cache:
                    target = TargetType(name=target_name)
                    session.add(target)
                    session.commit()
                    session.refresh(target)
                    target_cache[target_name] = target.id

                if attack_name not in attack_cache:
                    attack = AttackType(name=attack_name)
                    session.add(attack)
                    session.commit()
                    session.refresh(attack)
                    attack_cache[attack_name] = attack.id

                if region_name not in region_cache:
                    region = Region(name=region_name)
                    session.add(region)
                    session.commit()
                    session.refresh(region)
                    region_cache[region_name] = region.id


                if country_name not in country_cache:
                    country = Country(name=country_name, region_id=region_cache[region_name])
                    session.add(country)
                    session.commit()
                    session.refresh(country)
                    country_cache[country_name] = country.id

                city_key = (country_name, city_name)
                if city_key not in city_cache:
                    city = City(name=city_name, country_id=country_cache[country_name])
                    session.add(city)
                    session.commit()
                    session.refresh(city)
                    city_cache[city_key] = city.id

                location_key = (latitude, longitude)
                if location_key not in location_cache:
                    location = Location(
                        latitude=latitude,
                        longitude=longitude,
                        country_id=country_cache[country_name],
                        city_id=city_cache[city_key],
                        region_id=region_cache[region_name],
                    )
                    session.add(location)
                    session.commit()
                    session.refresh(location)
                    location_cache[location_key] = location.id

                casualties = Casualties(killed=killed, wounded=wounded)
                session.add(casualties)
                session.commit()


                event = Event(
                    location_id=location_cache[location_key],
                    year=year,
                    month=month,
                    day=day,
                    gang_name=gang_name,
                    total_terrorists=total_terrorists,
                    attack_type_id=attack_cache[attack_name],
                    target_type_id=target_cache[target_name],
                    casualties_id=casualties.id,
                    description=description
                )
                events.append(event)
                if i % 500 == 0:
                    print(f"Processed {i} rows")
                    session.bulk_save_objects(events)
                    session.commit()
                    events = []

            session.bulk_save_objects(events)
            session.commit()


if __name__ == '__main__':
    read_csv_data(r'C:\Users\ARI\PycharmProjects\FinalTest\data\merge.csv')
