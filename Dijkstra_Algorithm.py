from Network import Network
from node import Node

class Dijkstra:

    __start: Node
    __destination: Node
    __network: Network

    def __init__(self, network):
        self.__network = network

    def test(self):
        __not_visited_nodes = self.__network.get_nodes()
        for nodes in __not_visited_nodes:
            print(nodes)

    def run(self, start, destination):
        self.__start = start
        self.__destination = destination

