# We have seen how to implement min (and max) heaps from scratch.
# Your task is to check whether a list contains a valid min heap or not.
# The heap is a list data structure containing integers.
# Hint: you just have to check the heap properties (in a min heap the parent is smaller than the children)

# left child: 2i + 1 where i is the parent index
# right child: 2i + 2

def is_min_heap(heap):
    # No need to check leaf nodes because they do not have children (the formula above would lead to an error)
    # We check the items where 2i + 2 <= N (size of the array)
    items_count = ((len(heap)) - 2) // 2  # Wrong return value when the heap has less than 3 items

    for i in range(items_count):
        if heap[i] > heap[2 * i + 1] or heap[i] > heap[2 * i + 2]:
            return False

    return True
