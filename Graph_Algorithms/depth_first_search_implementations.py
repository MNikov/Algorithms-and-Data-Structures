class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


# We start from a given node, check its neighbours
# and keep on doing that for every one until the queue gets empty
# The graph is iterated branch by branch
def depth_first_search_1(start_node):
    stack = [start_node]

    while stack:
        actual_node = stack.pop()
        actual_node.visited = True
        print(actual_node.name)

        for neighbour in actual_node.adjacency_list:
            if not neighbour.visited:
                stack.append(neighbour)


def depth_first_search_2(start_node):
    stack = [start_node]
    start_node.visited = True

    while stack:
        actual_node = stack.pop()
        print(actual_node.name)

        for neighbour in actual_node.adjacency_list:
            if not neighbour.visited:
                neighbour.visited = True
                stack.append(neighbour)


# Recursive implementation
# The upper two go to the 'right sleeve' of the directed graph first
# whereas this one starts with the 'left' one
def depth_first_search_3(start_node):
    start_node.visited = True
    print(start_node.name)

    for neighbour in start_node.adjacency_list:
        if not neighbour.visited:
            depth_first_search_3(neighbour)
