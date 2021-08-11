class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def start_insert(self, data):
        new_node = Node(data)
        self.length += 1

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def end_insert(self, data):
        new_node = Node(data)
        self.length += 1

        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node

        current_node.next_node = new_node

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

    def present(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node


ll = LinkedList()
ll.start_insert(1)
ll.start_insert(2)
ll.end_insert(3)
ll.end_insert(4)
ll.present()
print(f'The length of the linked list is {ll.length}.')
ll.remove(4)
print(f'The length of the linked list is {ll.length}.')
ll.present()
