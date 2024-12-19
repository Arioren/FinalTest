from app.db.database import session_maker, engine
from app.db.model import TargetType, AttackType, Country, Region, City, Location, Casualties, Event, Base


def read_csv_data(file_path):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with session_maker() as session:
        with open(file_path, 'r', encoding='iso-8859-1') as file:
            for line in file.readlines()[1:]:
                data = line.split(',')
                target_type = session.query(TargetType).filter(TargetType.name == data[35]).first()
                if not target_type:
                    target_type = TargetType(name=data[35])
                    session.add(target_type)
                    session.commit()
                    session.refresh(target_type)
                attack_type = session.query(AttackType).filter(AttackType.name == data[29]).first()
                if not attack_type:
                    attack_type = AttackType(name=data[29])
                    session.add(attack_type)
                    session.commit()
                    session.refresh(attack_type)
                region = session.query(Region).filter(Region.name == data[10]).first()
                if not region:
                    region = Region(name=data[10])
                    session.add(region)
                    session.commit()
                    session.refresh(region)
                country = session.query(Country).filter(Country.name == data[8]).first()
                if not country:
                    country = Country(name=data[8], region_id=region.id)
                    session.add(country)
                    session.commit()
                    session.refresh(country)
                city = session.query(City).filter(City.name == data[12]).first()
                if not city:
                    city = City(name=data[12], country_id=country.id)
                    session.add(city)
                    session.commit()
                    session.refresh(city)
                try:
                    data[13] = float(data[13])
                except ValueError:
                    data[13] = None
                try:
                    data[14] = float(data[14])
                except ValueError:
                    data[14] = None
                location = session.query(Location).filter(Location.latitude == data[13], Location.longitude == data[14]).first()
                if not location:
                    location = Location(latitude=data[13], longitude=data[14], country_id=country.id, city_id=city.id, region_id=region.id)
                    session.add(location)
                    session.commit()
                    session.refresh(location)
                try:
                    casualties = Casualties(killed=float(data[98]))
                except ValueError:
                    casualties = Casualties(killed=0)
                try:
                    casualties.wounded = float(data[99])
                except ValueError:
                    casualties.wounded = 0

                session.add(casualties)
                session.commit()
                session.refresh(casualties)

                event = Event(location_id=location.id,
                              year=data[1],
                              month=data[2],
                              day=data[3],
                              gang_name=data[58],
                              attack_type_id=attack_type.id,
                              target_type_id=target_type.id,
                              casualties_id=casualties.id)
                session.add(event)
                session.commit()






                


