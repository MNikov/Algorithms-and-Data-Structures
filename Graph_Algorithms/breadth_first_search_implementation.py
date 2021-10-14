class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


# We start from a given node, check its neighbours
# and keep on doing that for every one until the queue gets empty
def breadth_first_search(start_node):
    queue = [start_node]

    while queue:
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)

        for neighbour in actual_node.adjacency_list:
            if not neighbour.visited:
                queue.append(neighbour)
