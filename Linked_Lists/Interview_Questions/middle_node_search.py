# Finding the middle node in a linked list overview
# Interview Question #7
# Suppose we have a standard linked list.
# Construct an in-place (without extra memory) algorithm thats able to find the middle node!

# NOTE: Both functions could be added to the linked list class, the references should be adjusted
import math


def find_mid_node_1(linked_list):
    current_node = linked_list.head
    mid = math.ceil(linked_list.length / 2)
    counter = 1

    while counter < mid:
        current_node = current_node.next_node
        counter += 1

    return current_node.data


# Course implementation
def find_mid_node_2(linked_list):
    fast_pointer = linked_list.head
    slow_pointer = linked_list.head

    while fast_pointer.next_node and fast_pointer.next_node.next_node:
        fast_pointer = fast_pointer.next_node.next_node
        slow_pointer = slow_pointer.next_node

    return slow_pointer.data
