class BubbleSort:
    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        for i in range(len(self.nums) - 1):
            for j in range(len(self.nums) - 1 - i):
                if self.nums[j] > self.nums[j + 1]:
                    self.nums[j], self.nums[j + 1] = self.nums[j + 1], self.nums[j]


alg = BubbleSort([1, -5, 0, 2, -1, 10, 9, 100, 56, -34])
alg.sort()
print(alg.nums)
