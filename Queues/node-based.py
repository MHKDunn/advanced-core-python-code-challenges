class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = self.tail

    def dequeue(self):
        if self.head is None:
            return None
        item = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return item
    
    def is_empty(self):
        return self.head is None
    
    

