import heapq  # Binary heap, not a Fibonacci one


class Edge:
    def __init__(self, weight, start_vertex, target):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target = target


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None  # The node we come from
        self.adjacency_list = []  # Contains edges
        self.min_distance = float('inf')  # Minimal distance from the starting node

    def __lt__(self, other):
        return self.min_distance < other.min_distance


class DijkstraAlgorithm:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)

        while self.heap:
            current_vertex = heapq.heappop(self.heap)
            if current_vertex.visited:  # This check has to be present because we reinsert
                continue  # nodes with new distance to the heap. Prevents revisiting.

            for edge in current_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.target
                new_distance = u.min_distance + edge.weight

                # Check for shorter path to v
                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    # Update heap
                    heapq.heappush(self.heap, v)

            current_vertex.visited = True

    @staticmethod
    def get_shortest_path(vertex):
        print(f'The shortest path to the given vertex is: {vertex.min_distance}')

        current_vertex = vertex
        while current_vertex:
            print(current_vertex.name)
            current_vertex = current_vertex.predecessor


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')
node7 = Node('G')
node8 = Node('H')

edge1 = Edge(5, node1, node2)
edge2 = Edge(8, node1, node8)
edge3 = Edge(9, node1, node5)
edge4 = Edge(15, node2, node4)
edge5 = Edge(12, node2, node3)
edge6 = Edge(4, node2, node8)
edge7 = Edge(7, node8, node3)
edge8 = Edge(6, node8, node6)
edge9 = Edge(5, node5, node5)
edge10 = Edge(4, node5, node6)
edge11 = Edge(20, node5, node7)
edge12 = Edge(1, node6, node3)
edge13 = Edge(13, node6, node7)
edge14 = Edge(3, node3, node4)
edge15 = Edge(11, node3, node7)
edge16 = Edge(9, node4, node7)

node1.adjacency_list.append(edge1)
node1.adjacency_list.append(edge2)
node1.adjacency_list.append(edge3)
node2.adjacency_list.append(edge4)
node2.adjacency_list.append(edge5)
node2.adjacency_list.append(edge6)
node8.adjacency_list.append(edge7)
node8.adjacency_list.append(edge8)
node5.adjacency_list.append(edge9)
node5.adjacency_list.append(edge10)
node5.adjacency_list.append(edge11)
node6.adjacency_list.append(edge12)
node6.adjacency_list.append(edge13)
node3.adjacency_list.append(edge14)
node3.adjacency_list.append(edge15)
node4.adjacency_list.append(edge16)

algorithm = DijkstraAlgorithm()
algorithm.calculate(node1)
algorithm.get_shortest_path(node6)
