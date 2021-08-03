# Interview Question #5
# The problem is that we want to find duplicates in a one-dimensional array of integers in O(N) running time
# where the integer values are smaller than the length of the array!
# For example: if we have a list [1, 2, 3, 1, 5] then the algorithm can detect that there are a duplicate with value 1.
# Note: the array can not contain items smaller than 0 and items with values greater than the size of the list.
# This is how we can achieve O(N) linear running time complexity!


def duplicate_finder_1(nums):
    duplicates = []

    for n in set(nums):
        if nums.count(n) > 1:
            duplicates.append(n)

    return duplicates if duplicates else 'The array does not contain any duplicates!'


def duplicate_finder_2(nums):
    duplicates = set()

    for i, n in enumerate(sorted(nums)):
        if i + 1 < len(nums) and n == nums[i + 1]:
            duplicates.add(n)

    return list(duplicates) if duplicates else 'The array does not contain any duplicates!'


# Course implementation
def duplicate_finder_3(nums):
    duplicates = set()
    for n in nums:
        if nums[abs(n)] >= 0:
            nums[abs(n)] *= -1
        else:
            duplicates.add(n)

    return list({-n if n < 0 else n for n in duplicates}) if duplicates \
        else 'The array does not contain any duplicates!'
    # return list(map(lambda n: n * -1 if n < 0 else n,
    #                 duplicates)) if duplicates else 'The array does not contain any duplicates!'


# My solutions allow the use of numbers greater than the length of the array
print(duplicate_finder_1([1, 2, 3, 4]))
print(duplicate_finder_1([1, 1, 2, 3, 3, 4]))
print(duplicate_finder_2([5, 6, 7, 8]))
print(duplicate_finder_2([5, 6, 6, 6, 7, 7, 9]))
print(duplicate_finder_3([2, 3, 1, 2, 4, 3, 3]))
print(duplicate_finder_3([0, 1, 2]))
