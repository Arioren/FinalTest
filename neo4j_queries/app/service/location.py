import pandas as pd

def find_coordinates_in_csv(file_path, country_name):
    try:
        countries = pd.read_csv(file_path, encoding="utf-8").filter(
            items=["Country", 'Latitude (average)', 'Longitude (average)']).to_dict(orient="records")
        countries_with_coordinates = {country['Country']: {**country} for country in countries}
        return countries_with_coordinates.get(country_name)
    except UnicodeDecodeError:
        return pd.read_csv(file_path, encoding="latin1").to_dict(orient="records")


countries_and_coordinates_path = r"C:\Users\ARI\PycharmProjects\FinalTest\neo4j_queries\app\data\countries_codes_and_coordinates.csv"
def get_country_coordinates(country_name):
    country = find_coordinates_in_csv(countries_and_coordinates_path, country_name)
    if country:
        return [float(country["Latitude (average)"].split('"')[1]),
                float(country["Longitude (average)"].split('"')[1])]