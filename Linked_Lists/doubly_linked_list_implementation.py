class Node:
    def __init__(self, data):
        self.data = data
        self.prev_node = None
        self.next_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def start_insert(self, data):
        new_node = Node(data)
        self.length += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev_node = new_node
            new_node.next_node = self.head
            self.head = new_node

    def end_insert(self, data):
        new_node = Node(data)
        self.length += 1

        if not self.tail:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    # It could be done starting from the tail too
    # Either way the running time remains O(N)
    def remove(self, data):
        if not self.head:
            return

        current_node = self.head
        previous_node = None

        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node

        # Item not present in the linked list
        if not current_node:
            return

        self.length -= 1

        if not previous_node:
            self.head = current_node.next_node  # We remove the 1st node
        else:
            previous_node.next_node = current_node.next_node

    def traverse_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def traverse_backward(self):
        current_node = self.tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev_node
