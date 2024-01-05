class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        dq = self.dequeue_stack
        eq = self.enqueue_stack

        if len(dq) == 0:
            while len(eq) > 0:
                item = eq.pop()
                dq.append(item)
        if len(dq) == 0:
            return None
        else:
            return dq.pop()
        
    def is_empty(self):
        dq = self.dequeue_stack
        eq = self.enqueue_stack
        return len(dq) == 0 and len(eq) == 0
    
    def size(self):
        dq = self.dequeue_stack
        eq = self.enqueue_stack
        return len(dq) + len(eq)