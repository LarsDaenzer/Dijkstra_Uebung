from Network import Network

path_dir: str = r"C:\Users\larsd\PycharmProjects\Dijkstra\DistanzenNeu.csv"

Map = Network.generate_network(str)

Nodes = Network.get_nodes()

for locations in Nodes:
    print(locations)
