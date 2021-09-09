class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data, None)
        else:
            self.__insert_node(data, self.root)

    def __insert_node(self, data, node):
        if data < node.data:
            if node.left_child:
                self.__insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
                node.height = max(self.__calc_height(node.left_child), self.__calc_height(node.right_child)) + 1
        else:
            if node.right_child:
                self.__insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)
                node.height = max(self.__calc_height(node.left_child), self.__calc_height(node.right_child)) + 1

        self.__handle_violation(node)

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
            if not node.left_child and not node.right_child:
                parent = node.parent

                if parent and parent.left_child == node:
                    parent.left_child = None
                elif parent and parent.right_child:
                    parent.right_child = None

                if not parent:
                    self.root = None

                del node

                self.__handle_violation(parent)

            elif not node.left_child and node.right_child:
                parent = node.parent

                if parent:
                    if parent.left_child == node:
                        parent.left_child = node.left_child
                    elif parent.right_child == node:
                        parent.right_child = node.right_child
                else:
                    self.root = node.right_child

                node.right_child.parent = parent
                del node

                self.__handle_violation(parent)

            elif node.left_child and not node.right_child:
                parent = node.parent

                if parent:
                    if parent.left_child == node:
                        parent.left_child = node.left_child
                    elif parent.right_child == node:
                        parent.right_child = node.right_child
                else:
                    self.root = node.left_child

                node.left_child.parent = parent
                del node

                self.__handle_violation(parent)

            else:
                predecessor = self.__get_predecessor(node.left_child)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.__remove_node(data, predecessor)

    def __handle_violation(self, node):
        # check the nodes from the node we have inserted up to the root
        while node:
            node.height = max(self.__calc_height(node.left_child), self.__calc_height(node.right_child)) + 1
            self.__violation_helper(node)
            # whenever we have a violation (rotation) there may be a violation in other parts of the tree
            node = node.parent

    def __get_predecessor(self, node):
        if node.right_child:
            return self.__get_predecessor(node.right_child)

        return node

    def __calc_height(self, node):
        if not node:
            return -1

        return node.height

    def __calc_balance(self, node):
        if not node:
            return 0

        return self.__calc_height(node.left_child) - self.__calc_height(node.right_child)

    def __violation_helper(self, node):
        balance = self.__calc_balance(node)

        # left heavy tree, could be left-right or left-left heavy
        if balance > 1:
            # left-right heavy case: left rotation on parent + right rotation on grandparent
            if self.__calc_balance(node.left_child) < 0:
                self.__rotate_left(node.left_child)

            # right rotation on grandparent (used also in left-left heavy case)
            self.__rotate_right(node)

        # right heavy tree, could be left-right or right-right heavy
        if balance < -1:
            # right-left heavy case: right rotation before a left one
            if self.__calc_balance(node.right_child) > 0:
                self.__rotate_right(node.right_child)

            # left rotation on grandparent (used also in right-right heavy case)
            self.__rotate_left(node)

    def __rotate_right(self, node):
        temp_left_child = node.left_child
        t = temp_left_child.right_child

        temp_left_child.right_child = node
        node.left_child = t

        if t:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_child
        temp_left_child.parent = temp_parent

        if temp_left_child.parent and temp_left_child.parent.left_child == node:
            temp_left_child.parent.left_child = temp_left_child

        if temp_left_child.parent and temp_left_child.parent.right_child == node:
            temp_left_child.parent.right_child = temp_left_child

        if node == self.root:
            self.root = temp_left_child

        node.height = max(self.__calc_height(node.left_child), self.__calc_height(node.right_child))
        temp_left_child.height = max(self.__calc_height(temp_left_child.left_child),
                                     self.__calc_height(temp_left_child.right_child)) + 1

    def __rotate_left(self, node):
        temp_right_child = node.right_child
        t = temp_right_child.left_child

        temp_right_child.left_child = node
        node.right_child = t

        if t:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_child
        temp_right_child.parent = temp_parent

        if temp_right_child.parent and temp_right_child.parent.left_child == node:
            temp_right_child.parent.left_child = temp_right_child

        if temp_right_child.parent and temp_right_child.parent.right_child == node:
            temp_right_child.parent.right_child = temp_right_child

        if node == self.root:
            self.root = temp_right_child

        node.height = max(self.__calc_height(node.left_child), self.__calc_height(node.right_child))
        temp_right_child.height = max(self.__calc_height(temp_right_child.left_child),
                                      self.__calc_height(temp_right_child.right_child)) + 1
