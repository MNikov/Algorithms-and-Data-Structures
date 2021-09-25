class Colour:
    RED = 1
    BLACK = 2


class Node:
    def __init__(self, data, parent=None, colour=Colour.RED):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = parent
        self.colour = colour


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            self.__settle_violation(self.root)
        else:
            self.__insert_node(data, self.root)

    def __insert_node(self, data, node):
        if data > node.data:
            if not node.right_child:
                node.right_child = Node(data, node)
                self.__settle_violation(node.right_child)
            else:
                self.__insert_node(data, node.right_child)
        elif data < node.data:
            if not node.left_child:
                node.left_child = Node(data, node)
                self.__settle_violation(node.left_child)
            else:
                self.__insert_node(data, node.left_child)

    def traverse(self):
        if self.root:
            self.__in_order_traversal(self.root)

    def __in_order_traversal(self, node):
        if node.left_child:
            self.__in_order_traversal(node.left_child)

        print(node.data)

        if node.right_child:
            self.__in_order_traversal(node.right_child)

    def __rotate_right(self, node):
        temp_left_node = node.left_child
        t = temp_left_node.right_child

        temp_left_node.right_child = node
        node.left_child = t

        if t:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent and temp_left_node.parent.left_child == node:
            temp_left_node.parent.left_child = temp_left_node
        if temp_left_node.parent and temp_left_node.parent.right_child == node:
            temp_left_node.parent.right_child = temp_left_node

        if node == self.root:
            self.root = temp_left_node

    def __rotate_left(self, node):
        temp_right_node = node.right_child
        t = temp_right_node.left_child

        temp_right_node.left_child = node
        node.right_child = t

        if t:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent and temp_right_node.parent.left_child == node:
            temp_right_node.parent.left_child = temp_right_node
        if temp_right_node.parent and temp_right_node.parent.right_child == node:
            temp_right_node.parent.right_child = temp_right_node

        if node == self.root:
            self.root = temp_right_node

    def __settle_violation(self, node):
        while node != self.root and self.__is_red(node) and self.__is_red(node.parent):
            parent_node = node.parent
            grandparent_node = parent_node.parent

            # Parent is a left child of its parent
            if parent_node == grandparent_node.left_child:
                uncle = grandparent_node.right_child

                # Recolouring
                if uncle and self.__is_red(uncle):
                    grandparent_node.colour = Colour.RED
                    parent_node.colour = Colour.BLACK
                    uncle.colour = Colour.BLACK
                    node = grandparent_node
                else:
                    # Uncle node is black and node is a right child
                    if node == parent_node.right_child:
                        self.__rotate_left(parent_node)
                        node = parent_node
                        parent_node = node.parent

                    # If it is not a right child -> rotation on the grandparent + parent and grandparent change colour
                    parent_node.colour = Colour.BLACK
                    grandparent_node.colour = Colour.RED
                    self.__rotate_right(grandparent_node)
            else:
                uncle = grandparent_node.left_child

                if uncle and self.__is_red(uncle):
                    grandparent_node.colour = Colour.RED
                    parent_node.colour = Colour.BLACK
                    uncle.colour = Colour.BLACK
                    node = grandparent_node
                else:
                    # Uncle node is black and node is a left child
                    if node == parent_node.left_child:
                        self.__rotate_right(parent_node)
                        node = parent_node
                        parent_node = node.parent

                    # If it is not a left child -> rotation on the grandparent + parent and grandparent change colour
                    parent_node.colour = Colour.BLACK
                    grandparent_node.colour = Colour.RED
                    self.__rotate_left(grandparent_node)

        if self.__is_red(self.root):
            self.root.colour = Colour.BLACK

    @staticmethod
    def __is_red(node):
        return node.colour == Colour.RED if node else False
