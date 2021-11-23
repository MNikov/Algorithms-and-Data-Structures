def insertion_sort(nums):
    for i in range(len(nums)):
        j = i

        # Swap the items on the left if they are bigger
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1


n = [-121, 21, 343, 8, 5, 1, 7]
insertion_sort(n)
print(n)
