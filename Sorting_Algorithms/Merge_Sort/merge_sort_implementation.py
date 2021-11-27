def merge_sort(nums):
    if len(nums) == 1:
        return

    middle_index = len(nums) // 2
    left_half = nums[:middle_index]
    right_half = nums[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            nums[k] = left_half[i]
            i += 1
        else:
            nums[k] = right_half[j]
            j += 1

        k += 1

    # We do this in case are left over items in some of the arrays
    while i < len(left_half):
        nums[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        nums[k] = right_half[j]
        j += 1
        k += 1


n = [3, 2, 1, -123, 88, 53]
merge_sort(n)
print(n)
