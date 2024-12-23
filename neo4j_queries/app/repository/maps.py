import folium

from neo4j_queries.app.service.location import get_country_coordinates

same_target_path = r'C:\Users\ARI\PycharmProjects\FinalTest\neo4j_queries\app\templates\same_target.html'
same_strategy_path =r'C:\Users\ARI\PycharmProjects\FinalTest\neo4j_queries\app\templates\same_strategy.html'
high_groups_path = r'C:\Users\ARI\PycharmProjects\FinalTest\neo4j_queries\app\templates\high_groups.html'
wide_influence_path = r'C:\Users\ARI\PycharmProjects\FinalTest\neo4j_queries\app\templates\wide_influence.html'

# 11
def groups_with_same_target_to_mup(same_targets):
    initial_location = get_country_coordinates(same_targets[0]["country"])
    map = folium.Map(location=initial_location)

    for target in same_targets:
        coordinates = get_country_coordinates(target["country"])
        if coordinates and coordinates[0] and coordinates[1]:
            folium.Marker(coordinates,
                          popup=f'groups: {target['groups']}, \n target: {target['target']}').add_to(map)

    map.save(same_target_path)


# 14

def same_strategy_to_mup(same_strategies):
    initial_location = get_country_coordinates(same_strategies[0]["country"])
    map = folium.Map(location=initial_location)

    for target in same_strategies:
        coordinates = get_country_coordinates(target["country"])
        if coordinates and coordinates[0] and coordinates[1]:
            folium.Marker(coordinates,
                          popup=f'groups: {target['groups']}, \n type: {target['type']}').add_to(map)

    map.save(same_strategy_path)

# 16
def high_groups_to_mup(high_groups):
    initial_location = get_country_coordinates(high_groups[0]["countries"][0]['name'])
    map = folium.Map(location=initial_location)

    for group in high_groups:
        for country in group['countries']:
            coordinates = get_country_coordinates(country['name'])
            if coordinates and coordinates[0] and coordinates[1]:
                folium.Marker(coordinates,
                              popup=f'country_count: {group['country_count']}, \n group: {group['group']}, \n '
                                    f'target_count: {group['target_count']}, \n type_c'
                                    f'ount: {group['type_count']}').add_to(map)

    map.save(high_groups_path)


# 18
def groups_with_wide_influence_to_mup(wide_influences):
    initial_location = get_country_coordinates(wide_influences[0]["country"])
    map = folium.Map(location=initial_location)

    for country in wide_influences:
        coordinates = get_country_coordinates(country['country'])
        if coordinates and coordinates[0] and coordinates[1]:
            folium.Marker(coordinates,
                          popup=f'group_count: {country['group_count']}, \n groups: {country['groups']},').add_to(map)

    map.save(wide_influence_path)