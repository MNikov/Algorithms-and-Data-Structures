# Reverse a linked list in-place overview
# Interview Question #8
# Construct an in-place algorithm to reverse a linked list!

# Quite bad implementation, left it so as to show what practices to avoid
def reverse_1(linked_list):
    current_node = linked_list.head
    reversed_ll = ''  # Added to prevent errors, use the one below
    # reversed_ll = LinkedList()  # The class is not present in this file

    while current_node:
        reversed_ll.start_insert(current_node.data)
        current_node = current_node.next_node

    linked_list = reversed_ll
    return linked_list


# Course implementation
def reverse_2(linked_list):
    current_node = linked_list.head
    prev_node = None
    next_node = None

    while current_node:
        next_node = current_node.next_node
        current_node.next_node = prev_node
        prev_node = current_node
        current_node = next_node

    linked_list.head = prev_node
