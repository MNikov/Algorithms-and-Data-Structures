class QuickSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        self.__quicksort(0, len(self.data) - 1)

    def __quicksort(self, low, high):
        if low >= high:
            return

        pivot_index = self.__partition(low, high)
        self.__quicksort(low, pivot_index - 1)
        self.__quicksort(pivot_index + 1, high)

    def __partition(self, low, high):
        # We use the middle item as a pivot
        pivot_index = (low + high) // 2

        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]

        for j in range(low, high):
            if self.data[j] <= self.data[high]:
                self.data[low], self.data[j] = self.data[j], self.data[low]
                low += 1

        self.data[low], self.data[high] = self.data[high], self.data[low]

        return low


alg = QuickSort([3, 321, -3, 432, 2, 0, 65])
alg.sort()
print(alg.data)
