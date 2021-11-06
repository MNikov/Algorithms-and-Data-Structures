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
        self.has_cycle = False

    def find_shortest_path(self):
        self.start_vertex.min_distance = 0

        # We do V-1 iterations because the most complex possible way from one vertex to another
        # could be through all vertices.
        # ABCDE graph: in order to reach E starting from a we may have to visit BCDE which is V-1 vertices
        for _ in range(len(self.vertex_list) - 1):
            for edge in self.edge_list:
                # Calculate whether there are shorter paths
                u = edge.start_vertex
                v = edge.target_vertex
                dist = u.min_distance + edge.weight

                if dist < v.min_distance:
                    v.predecessor = u
                    v.min_distance = dist

        # Check for negative cycle
        for edge in self.edge_list:
            if self.__check_cycle(edge):
                print('Negative cycle detected...')
                return

    def __check_cycle(self, edge):
        # If the total cost (min_distance) of a given vertex decreases after V-1 iterations,
        # there is a negative cycle
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


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')
node7 = Node('G')

edge1 = Edge(5, node1, node2)
edge2 = Edge(9, node1, node5)
edge3 = Edge(4, node2, node5)
edge4 = Edge(12, node2, node3)
edge5 = Edge(7, node2, node4)
edge6 = Edge(3, node3, node4)
edge7 = Edge(1, node3, node6)
edge8 = Edge(9, node4, node7)
edge9 = Edge(6, node5, node3)
edge10 = Edge(4, node5, node6)
edge11 = Edge(2, node6, node7)
# edge12 = Edge(6, node7, node3)
edge12 = Edge(-6, node7, node3)

node1.adjacency_list.append(edge1)
node1.adjacency_list.append(edge2)
node2.adjacency_list.append(edge3)
node2.adjacency_list.append(edge4)
node2.adjacency_list.append(edge5)
node3.adjacency_list.append(edge6)
node3.adjacency_list.append(edge7)
node4.adjacency_list.append(edge8)
node5.adjacency_list.append(edge9)
node5.adjacency_list.append(edge10)
node6.adjacency_list.append(edge11)
node7.adjacency_list.append(edge12)

vertices = (node1, node2, node3, node4, node5, node6, node7)
edges = (edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12)

alg = BellmanFordAlgorithm(vertices, edges, node1)
alg.find_shortest_path()
alg.get_shortest_path(node7)
