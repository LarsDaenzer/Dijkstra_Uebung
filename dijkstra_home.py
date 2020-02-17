from Network import Network

str = "C:/Users/larsd/PycharmProjects/Dijkstra/DistanzenNeu.csv"

print(str)
network = Network(str)

Nodes = network.get_nodes()

for locations in Nodes:
    print(locations)
