import json
def findStations(stations):
    station_dict = {}
    for station in stations:
        station_dict[station["Name"]] = set(station["Cities"])
    
    cities_to_cover = set(all_cities)
    selected_stations = []
    
    while cities_to_cover and any(cities_to_cover & cities for cities in station_dict.values()):
        best_station = None
        covered_cities = set()
        for station, cities in station_dict.items():
            if station in selected_stations:
                continue
            new_covered = cities_to_cover & cities
            if len(new_covered) > len(covered_cities):
                best_station = station
                covered_cities = new_covered
        if not covered_cities:
            break
        selected_stations.append(best_station)
        cities_to_cover -= covered_cities
    return sorted(selected_stations)

all_cities = json.loads(input())
n = int(input())
stations = []

for _ in range(n):
    station = json.loads(input())
    stations.append(station)

result = findStations(stations)
print(result)
