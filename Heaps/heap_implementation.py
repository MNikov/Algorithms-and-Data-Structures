CAPACITY = 10


# Max heap
class Heap:
    def __init__(self):
        self.size = 0
        # Underlying list
        self.heap = [0] * CAPACITY

    def insert(self, item):
        if self.size == CAPACITY:
            return

        self.heap[self.size] = item
        self.size += 1

        self.__fix_up(self.size - 1)

    # Check whether the order is correct (the root must be the biggest item), going from the bottom to the root
    def __fix_up(self, index):
        parent_index = (index - 1) // 2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.__fix_up(parent_index)

    def get_max(self):
        return self.heap[0]

    # Remove the root, swap it with the last item and check for violations
    def poll(self):
        max_item = self.get_max()

        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        self.size -= 1

        self.__fix_down(0)

        return max_item

    # Similar to __fix_up but starting from the top (root)
    def __fix_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        largest_index = index

        if left_index < self.size and self.heap[left_index] > self.heap[index]:
            largest_index = left_index

        if right_index < self.size and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index

        # Check whether the parent is the biggest and terminate the recursion
        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.__fix_down(largest_index)

    # O(NlogN)
    def heap_sort(self):
        for _ in range(self.size):
            max_item = self.poll()
            print(max_item)
