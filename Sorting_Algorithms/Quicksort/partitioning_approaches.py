# Hoare's partitioning and Lomuto's partitioning
# In out quicksort implementation we used the so-called Lomuto approach. So there is a crucial difference between
# the original Hoare's partitioning and Lomuto's partitioning (which is easier to comprehend and to implement)

# algorithm
# partition(A, lo, hi) is
#
# pivot := A[hi]
# i := lo
#
# for j := lo to hi - 1 do
# if A[j] < pivot then
# swap
# A[i]
# with A[j]
#     i := i + 1
#
# swap
# A[i]
# with A[hi]
#
# return i

# So this is exactly what we have implemented - the so-called Lomuto's approach.
# What is the original Hoare's implementation for partitioning?

# algorithm
# partition(A, lo, hi) is
#
# pivot := A[lo + (hi - lo) / 2]
#
# i := lo - 1
# j := hi + 1
#
# loop
# forever
# do
# i := i + 1
# while A[i] < pivot
#
# do
# j := j - 1
# while A[j] > pivot
#
# if i >= j then
# return j
#
# swap
# A[i]
# with A[j]

# As you can see Hoare's approach uses 2 indexes during the implementation.
#
# NOTE: both of the approaches are the same in the sense that O(NxN) quadratic running time may happen in worst-case.
#
# CRUCIAL DIFFERENCE (!!!): Hoare’s implementation is more efficient because it does 3x fewer swaps on average and
# it creates efficient partitions even when all values are equal
