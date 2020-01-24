from Network import Network
import os


path = os.path('C:\Users\larsd\PycharmProjects\Dijkstra\DistanzenNeu.csv')

Map = Network.generate_network(path)

Nodes = Network.get_nodes()

for locations in Nodes:
    print(locations)



