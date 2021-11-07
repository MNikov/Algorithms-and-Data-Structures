# Detecting negative cycles on the FOREX
# We can find the shortest path in a given G(V,E) graph with Dijkstra's algorithm
# and we can handle even negative edge weights with Bellman-Ford approach.
# Let's use Bellman-Ford approach to find negative cycles on the FOREX!
import math


class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.predecessor = None
        self.min_distance = float('inf')


class BellmanFordAlgorithm:
    def __init__(self, vertex_list, edge_list, start_vertex):
        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.start_vertex = start_vertex
        self.cycle_list = []
        self.has_cycle = False

    def find_shortest_path(self):
        self.start_vertex.min_distance = 0

        for _ in range(len(self.vertex_list) - 1):
            for edge in self.edge_list:
                u = edge.start_vertex
                v = edge.target_vertex
                dist = u.min_distance + edge.weight

                if dist < v.min_distance:
                    v.predecessor = u
                    v.min_distance = dist

        for edge in self.edge_list:
            if self.__check_cycle(edge):
                print('Negative cycle detected...')

                vertex = edge.start_vertex
                while vertex is not edge.target_vertex:
                    self.cycle_list.append(vertex)
                    vertex = vertex.predecessor

                self.cycle_list.append(edge.target_vertex)
                for v in self.cycle_list:
                    print(v.name)
                return

    def __check_cycle(self, edge):
        if edge.start_vertex.min_distance + edge.weight < edge.target_vertex.min_distance:
            self.has_cycle = True
            return True
        return False

    def get_shortest_path(self, vertex):
        if not self.has_cycle:
            print(f'Shortest path exists with value: {vertex.min_distance}')
            node = vertex
            while node:
                print(node.name)
                node = node.predecessor
        else:
            print('There is a negative cycle in the graph!')


node0 = Node('USD')
node1 = Node('EUR')
node2 = Node('GBP')
node3 = Node('CHF')
node4 = Node('CAD')

edge1 = Edge(-1 * math.log(0.741), node0, node1)
edge2 = Edge(-1 * math.log(0.657), node0, node2)
edge3 = Edge(-1 * math.log(1.061), node0, node3)
edge4 = Edge(-1 * math.log(1.005), node0, node4)

edge5 = Edge(-1 * math.log(1.349), node1, node0)
edge6 = Edge(-1 * math.log(0.888), node1, node2)
edge7 = Edge(-1 * math.log(1.433), node1, node3)
edge8 = Edge(-1 * math.log(1.366), node1, node4)

edge9 = Edge(-1 * math.log(1.521), node2, node0)
edge10 = Edge(-1 * math.log(1.126), node2, node1)
edge11 = Edge(-1 * math.log(1.614), node2, node3)
edge12 = Edge(-1 * math.log(1.538), node2, node4)

edge13 = Edge(-1 * math.log(0.942), node3, node0)
edge14 = Edge(-1 * math.log(0.698), node3, node1)
edge15 = Edge(-1 * math.log(0.619), node3, node2)
edge16 = Edge(-1 * math.log(0.953), node3, node4)

edge17 = Edge(-1 * math.log(0.995), node4, node0)
edge18 = Edge(-1 * math.log(0.732), node4, node1)
edge19 = Edge(-1 * math.log(0.650), node4, node2)
edge20 = Edge(-1 * math.log(1.049), node4, node3)

node0.adjacency_list.append(edge1)
node0.adjacency_list.append(edge2)
node0.adjacency_list.append(edge3)
node0.adjacency_list.append(edge4)
node1.adjacency_list.append(edge5)
node1.adjacency_list.append(edge6)
node1.adjacency_list.append(edge7)
node1.adjacency_list.append(edge8)
node2.adjacency_list.append(edge9)
node2.adjacency_list.append(edge10)
node2.adjacency_list.append(edge11)
node2.adjacency_list.append(edge12)
node3.adjacency_list.append(edge13)
node3.adjacency_list.append(edge14)
node3.adjacency_list.append(edge15)
node3.adjacency_list.append(edge16)
node4.adjacency_list.append(edge17)
node4.adjacency_list.append(edge18)
node4.adjacency_list.append(edge19)
node4.adjacency_list.append(edge20)

vertices = (node1, node2, node3, node4)
edges = (edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10,
         edge11, edge12, edge13, edge14, edge15, edge16, edge17, edge18, edge19, edge20)

alg = BellmanFordAlgorithm(vertices, edges, node1)
alg.find_shortest_path()
alg.get_shortest_path(node2)
