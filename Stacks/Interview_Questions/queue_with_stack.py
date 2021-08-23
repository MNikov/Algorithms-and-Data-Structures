# Queue with stack problem
# The aim is to design a queue abstract data type with the help of stacks.

# Course implementation
class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if not self.enqueue_stack and not self.dequeue_stack:
            return

        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()
