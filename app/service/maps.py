from typing import List
import folium
import os

def get_marker_color(fatal_avg: float) -> str:
    if fatal_avg < 1:
        return "green"
    elif 1 <= fatal_avg < 2:
        return "lightgreen"
    elif 2 <= fatal_avg < 4:
        return "orange"
    elif 4 <= fatal_avg < 6:
        return "darkorange"
    elif 6 <= fatal_avg <= 8:
        return "red"
    else:
        return "black"


def map_of_average_casualties(res: List[dict]) -> folium.Map:
    main_map = folium.Map(location=[0, 0], zoom_start=2)
    for loc in res:
        marker_color = get_marker_color(loc["average_casualties"])
        tooltip_text = (
            f"Region: {loc['region']}<br>"
            f"Average Casualties: {loc['average_casualties']:.2f}"
        )
        folium.Marker(
            location=[loc['latitude'], loc['longitude']],
            tooltip=tooltip_text,
            icon=folium.Icon(color=marker_color),
        ).add_to(main_map)

    save_path = r"C:\Users\ARI\PycharmProjects\FinalTest\htmls\average_by_region.html"
    os.remove(save_path)
    main_map.save(save_path)

    return main_map
