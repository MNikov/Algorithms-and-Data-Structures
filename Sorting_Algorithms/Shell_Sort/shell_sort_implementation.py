# Similar to the insertion sort but with less shifts thanks to the use of the gap
def shell_sort(nums):
    gap = len(nums) // 2

    while gap > 0:
        for i in range(gap, len(nums)):
            j = i

            while j >= gap and nums[j - gap] > nums[j]:
                nums[j], nums[j - gap] = nums[j - gap], nums[j]
                j -= gap

        gap //= 2


n = [4, 2, 5, 123, -15, 1]
shell_sort(n)
print(n)
