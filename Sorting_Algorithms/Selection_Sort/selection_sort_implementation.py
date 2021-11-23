def selection_sort(nums):
    for i in range(len(nums) - 1):
        index = i

        for j in range(i, len(nums)):
            if nums[j] < nums[index]:
                index = j

        # Swap the left-most item with the min item
        if index != i:
            nums[index], nums[i] = nums[i], nums[index]


n = [5, 4, 3, 2, 1]
selection_sort(n)
print(n)
