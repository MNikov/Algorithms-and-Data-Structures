class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data, None)
        else:
            self.__insert_node(data, self.root)

    def __insert_node(self, data, parent):
        if data < parent.data:
            if not parent.left_child:
                parent.left_child = Node(data, parent)
            else:
                self.__insert_node(data, parent.left_child)
        else:
            if not parent.right_child:
                parent.right_child = Node(data, parent)
            else:
                self.__insert_node(data, parent.right_child)

    def remove(self, data):
        if self.root:
            self.__remove_node(data, self.root)

    def __remove_node(self, data, node):
        if not node:
            return

        if data < node.data:
            self.__remove_node(data, node.left_child)
        elif data > node.data:
            self.__remove_node(data, node.right_child)
        else:
            # Removing a leaf node
            if not node.left_child and not node.right_child:
                parent = node.parent

                # Check whether it is left or right child
                if parent and parent.left_child == node:
                    parent.left_child = None
                if parent and parent.right_child == node:
                    parent.right_child = None

                # If the node is the root itself
                if not parent:
                    self.root = None

                del node

            # Removing a node with a single right child
            elif not node.left_child and node.right_child:
                parent = node.parent

                if parent:
                    if parent.left_child == node:
                        parent.left_child = node.right_child
                    if parent.right_child == node:
                        parent.right_child = node.right_child
                else:
                    self.root = node.right_child

                node.right_child.parent = parent
                del node

            # Removing a node with a single left child
            elif not node.right_child and node.left_child:
                parent = node.parent

                if parent:
                    if parent.left_child == node:
                        parent.left_child = node.left_child
                    if parent.right_child == node:
                        parent.right_child = node.left_child
                else:
                    self.root = node.left_child

                node.left_child.parent = parent
                del node

            # Removing a node with 2 children
            # by using the largest item in the left subtree (predecessor)
            # and swapping it with the root thus having to remove just a leaf node
            else:
                predecessor = self.__get_predecessor(node.left_child)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.__remove_node(data, predecessor)

    def __get_predecessor(self, node):
        if node.right_child:
            return self.__get_predecessor(node.right_child)

        return node

    def traverse(self):
        if self.root:
            self.__traverse_in_order(self.root)

    def __traverse_in_order(self, node):
        if node.left_child:
            self.__traverse_in_order(node.left_child)

        print(node.data)

        if node.right_child:
            self.__traverse_in_order(node.right_child)

    def get_max(self):
        if self.root:
            print(self.__find_max_value(self.root))

    def __find_max_value(self, node):
        if node.right_child:
            return self.__find_max_value(node.right_child)

        return node.data

    def get_min(self):
        print(self.__find_min_value(self.root))

    def __find_min_value(self, node):
        if node.left_child:
            return self.__find_min_value(node.left_child)

        return node.data
