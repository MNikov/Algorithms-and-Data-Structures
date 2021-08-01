# Interview Question #1
# The problem is that we want to reverse a T[] array in O(N) linear time complexity and
# we want the algorithm to be in-place as well - so no additional memory can be used!
# For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

def reverse_array_1(arr):
    return arr[::-1]


def reverse_array_2(arr):
    reversed_arr = []
    while arr:
        reversed_arr.append(arr.pop())
    return reversed_arr


# Course implementation
def reverse_array_3(arr):
    start_idx = 0
    end_idx = len(arr) - 1

    while start_idx < end_idx:
        temp = arr[start_idx]
        arr[start_idx] = arr[end_idx]
        arr[end_idx] = temp
        # or arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]
        start_idx += 1
        end_idx -= 1

    return arr


print(reverse_array_1([1, 2, 3, 4, 5]))
print(reverse_array_2([1, 2, 3, 4, 5]))
print(reverse_array_3([1, 2, 3, 4, 5]))
