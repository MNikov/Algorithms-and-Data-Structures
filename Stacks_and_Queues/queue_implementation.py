class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            el_to_go = self.queue[0]
            self.queue = self.queue[1:]
            # del self.queue[0] <- Alternative
            return el_to_go

    def peek(self):
        return self.queue[0] if self.queue else None
