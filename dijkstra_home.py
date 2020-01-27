from Network import Network

str = "C:/Users/larsd/PycharmProjects/Dijkstra/DistanzenNeu.csv"

print(str)

Map = 0
Network.generate_network(Map,str)

Nodes = Network.get_nodes(Map)

for locations in Nodes:
    print(locations)
