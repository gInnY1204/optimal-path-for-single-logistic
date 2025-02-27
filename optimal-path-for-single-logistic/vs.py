import folium
import numpy as np
import pandas as pd

def visualization(func, route, alpha, beta, gamma):
    # central coordinate of New York City
    central_lat, central_lng = 40.78554, -73.95956

    # visualization
    m = folium.Map(location=(central_lat, central_lng), zoom_start=10)
    m_ = folium.Map(location=(central_lat, central_lng), zoom_start=10)

    locs = []
    for idx in range(len(route)-1):
        func.init()
        print("astar_path_start")
        func.astar_path(route[idx], route[idx+1])
        path_detail = pd.read_csv("./result/optimal_shortest_path.csv")
        print("read_csv")
        lat_path = list(path_detail["latitude"])
        lng_path = list(path_detail["longitude"])
        locs.append([lat_path[0], lng_path[0]])
        print("location append")

        folium.PolyLine(locations=np.array([lat_path, lng_path]).T, smooth_factor=1.0, weight=2.0, color='blue').add_to(m)
        folium.CircleMarker(location=[lat_path[0], lng_path[0]], radius=3.0, color="blue", fill=True).add_to(m)
        folium.CircleMarker(location=[lat_path[0], lng_path[0]], radius=3.0, color="blue", fill=True).add_to(m_)

    locs.append([lat_path[-1], lng_path[-1]])
    folium.CircleMarker(location=[lat_path[-1], lng_path[-1]], radius=3.0, color="blue", fill=True).add_to(m)
    folium.CircleMarker(location=[lat_path[-1], lng_path[-1]], radius=3.0, color="blue", fill=True).add_to(m_)
    folium.PolyLine(locations=locs, smooth_factor=1.0, weight=2.0, color='blue').add_to(m_)

    m.save("./result/paths_2.html")
    m_.save("./result/sequence_2.html")