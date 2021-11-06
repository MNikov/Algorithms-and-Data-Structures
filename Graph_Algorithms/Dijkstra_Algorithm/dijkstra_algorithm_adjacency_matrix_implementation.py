import sys


class DijkstraAlgorithm:
    # Each vertex is represented as an integer(index)
    def __init__(self, adjacency_matrix, start_vertex):
        self.adjacency_matrix = adjacency_matrix
        self.start_vertex = start_vertex
        self.v = len(adjacency_matrix)  # Num of vertices
        self.visited = [False for _ in range(len(adjacency_matrix))]
        self.distances = [float('inf') for _ in range(len(adjacency_matrix))]
        self.distances[start_vertex] = 0

    def __get_min_vertex(self):
        # Find the vertex with the lowest distance
        min_vertex_value = sys.maxsize
        min_vertex_index = 0

        for index in range(self.v):
            if not self.visited[index] and self.distances[index] < min_vertex_value:
                min_vertex_value = self.distances[index]
                min_vertex_index = index

        return min_vertex_index

    def calculate(self):
        for vertex in range(self.v):
            current_vertex = self.__get_min_vertex()
            print(f'Considering vertex: {current_vertex}')
            self.visited[current_vertex] = True

            for other_vertex in range(self.v):
                # Check for connection between the 2 nodes
                if self.adjacency_matrix[current_vertex][other_vertex] > 0:
                    if self.distances[current_vertex] + self.adjacency_matrix[current_vertex][other_vertex] < \
                            self.distances[other_vertex]:
                        self.distances[other_vertex] = self.distances[current_vertex] + \
                                                       self.adjacency_matrix[current_vertex][other_vertex]

    def print_distances(self):
        print(self.distances)


m = [
    [0, 7, 5, 2, 0, 0],
    [7, 0, 0, 0, 3, 8],
    [5, 0, 0, 10, 4, 0],
    [2, 0, 10, 0, 0, 2],
    [0, 3, 4, 0, 0, 6],
    [0, 8, 0, 2, 6, 0],
]

alg = DijkstraAlgorithm(m, 1)
alg.calculate()
alg.print_distances()
