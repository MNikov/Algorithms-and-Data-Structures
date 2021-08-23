# Max in a stack problem overview
# The aim is to design an algorithm that can return the maximum item of a stack in O(1) running time complexity.
# We can use O(N) extra memory!
# Hint: we can use another stack to track the max item!

def stack_max(stack):
    return sorted(stack)[-1]


# Course implementation
class MaxStack:
    def __init__(self):
        self.stack = []
        self._max_stack = []

    def push(self, data):
        self.stack.append(data)

        if len(self.stack) == 1:
            self._max_stack.append(data)
            return

        if data > self._max_stack[-1]:
            self._max_stack.append(data)
        else:
            self._max_stack.append(self._max_stack[-1])

    def pop(self):
        self._max_stack.pop()
        return self.stack.pop()

    def get_max_item(self):
        return self._max_stack[-1]
