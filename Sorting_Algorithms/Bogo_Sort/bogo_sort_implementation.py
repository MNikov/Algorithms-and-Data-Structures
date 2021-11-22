import random


# The algorithm could be deterministic (presenting all possible permutations) and randomized (shown below).
# The latter one generates random permutations. Both that O(N!) running time.
class BogoSort:
    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        while not self.__is_sorted():
            self.__shuffle()

    def __is_sorted(self):
        for i in range(len(self.nums) - 1):
            if self.nums[i] > self.nums[i + 1]:
                return False
        return True

    # Fisher-Yates approach, generates a new permutation in O(N) and is in-place
    def __shuffle(self):
        for i in range(len(self.nums) - 2, -1, -1):
            j = random.randint(0, i + 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


alg = BogoSort([1, -4, 0, 10, 12, -5, 1, 2, -1, 34])
alg.sort()
print(alg.nums)
