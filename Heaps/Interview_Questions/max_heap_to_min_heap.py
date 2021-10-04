# Your task is to transform a max heap to a min heap!

class HeapTransformer:
    def __init__(self, heap):
        self.heap = heap

    def transform(self):
        for i in range((len(self.heap) - 2) // 2, -1, -1):
            self.__fix_down(i)

    def __fix_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        smallest_index = index

        if left_index < len(self.heap) and self.heap[left_index] < self.heap[index]:
            smallest_index = left_index

        if right_index < len(self.heap) and self.heap[right_index] < self.heap[smallest_index]:
            smallest_index = right_index

        # Check whether the parent is the smallest and terminate the recursion
        if index != smallest_index:
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            self.__fix_down(smallest_index)
