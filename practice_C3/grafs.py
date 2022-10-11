Stations = {
    "Адмиралтейская": {
        "Садовая": 4},
    "Садовая": {
        "Сенная площадь": 4,
        "Спасская": 3,
        "Адмиралтейская": 4,
        "Звенигородская": 5},
    "Сенная площадь": {
        "Садовая": 4,
        "Спасская": 4},
    "Спасская": {
        "Садовая": 3,
        "Сенная площадь": 4,
        "Достоевская": 6},
    "Звенигородская": {
        "Пушкинская": 3,
        "Садовая": 5},
    "Пушкинская": {
        "Звенигородская": 3,
        "Владимирская": 4},
    "Владимирская": {
        "Достоевская": 3,
        "Пушкинская": 4},
    "Достоевская": {
        "Владимирская": 3,
        "Спасская": 6}
}

start_station = 'Адмиралтейская'
Distance = {k: 100 for k in Stations.keys()}
Distance[start_station] = 0
Watching = {k: False for k in Stations.keys()}
Ancestors = {k: None for k in Stations.keys()}
#print(start_station)

for _ in range(len(Distance)):
    near_station = min([station for station in Watching.keys() if not Watching[station]], key=lambda x: Distance[x])
#    print(f'   {near_station}')
    for s in Stations[near_station].keys():

        if Distance[s] > Distance[near_station] + Stations[near_station][s]:
            Distance[s] = Distance[near_station] + Stations[near_station][s]
            Ancestors[s] = near_station



#    print(f'      {min(Stations[near_station], key=lambda x: Stations[near_station][x])}')
    Watching[near_station] = True

print(Ancestors)
#print(sorted(Distance, key=lambda x: Distance[x]))
pointer = 'Владимирская' # куда должны прийти
path = [] # список с вершинами пути
while pointer is not None: # перемещаемся, пока не придём в стартовую точку
    path.append(pointer)
    pointer = Ancestors[pointer]

path.reverse() # разворачиваем путь
print(path)