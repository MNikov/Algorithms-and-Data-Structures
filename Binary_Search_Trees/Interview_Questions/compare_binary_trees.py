# Write an efficient algorithm that is able to compare two binary search trees.
# The method returns true if the trees are identical (same topology with same values in the nodes)
# otherwise it returns false.

def compare(node1, node2):
    if not node1 or not node2:
        return node1 == node2

    if node1.data != node2.data:
        return False

    return compare(node1.left_child, node2.left_child) and compare(node1.right_child, node2.right_child)
