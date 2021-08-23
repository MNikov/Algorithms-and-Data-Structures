class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            el_to_go = self.stack[-1]
            self.stack = self.stack[:-1]
            # del self.stack[-1] <- Alternative
            return el_to_go

    def peek(self):
        return self.stack[-1] if self.stack else None

    def length(self):
        return len(self.stack)
