from Network import Network
from node import Node

class Dijkstra:

    __start: Node
    __destination: Node
    __network: Network

    def __init__(self,network):
        self.__network = network
        self.str = "C:/Users/larsd/PycharmProjects/Dijkstra/DistanzenNeu.csv"


    def test(self,network):
        network = Network(str)
        __not_visited_nodes = self.network.get_nodes()
        for nodes in __not_visited_nodes:
            print(nodes)

    def run(self,start,destination):