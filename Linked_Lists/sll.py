class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"<SLLNode object: data={self.data}, type={type(self.data)}>"

    def get_data(self):
        """
        Return the attribute self.data
        """
        
        return self.data

    def set_data(self, new_data):
        """
        Replace existing of self.data with new_data parameter
        """
        self.data = new_data

    def get_next(self):
        """
        Return the attribute self.next
        """

        return self.next

    def set_next(self, new_next):
        """ 
        Replace existing of self.next with new_next parameter
        """

        self.next = new_next

# node = SLLNode("apple")
# print(node.get_data())
# node.set_data(7)
# print(node.get_data())
# new_node = SLLNode("carrot")
# node.set_next(new_node)
# print(node.get_next())


class SLL:
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        return f"<SSL object: head={self.head} type={type(self.head)}>"

    def is_empty(self):
        """
        Returns True if linked list is empty else returns True
        """
        return self.head is None 
    
    def add_front(self, new_data):
        """ 
        Add node whose data is the new_data argument to the front of the Linked List
        """

        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """
        This function traverses the Linked List and returns an integer value 
        representing the number of nodes in the Linked List 

        The time complexity is 0(n) because every Node in the Linked List must 
        be visited in order to calculate the size of the Linked List
        """

        size = 0
        if self.head is None:
            return size
        
        current = self.head
        while current is not None: #while still Nodes left to count
            size += 1
            current = current.get_next()
        
        return size


    def search(self, data):
        """ 
        Traverses the Linked List and returns True if the data searched for is present in one of the Nodes.  
        Otherwise it returns False.

        The time complexity is 0(n) because in the worst case we have to search all Nodes. 
        """

        if self.head is None:
            return "Linked List is empty. No Nodes to search"
        
        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()

        return False

    def remove(self, data):
        """ 
        Removes the first occurrence of a Node that contains the argument as its self.data variable.  
        Returns nothing

        The time complexity is 0(n) because in the worst case we have to visit 
        every Node before we find the one we need to remove
        """

        if self.head is None:
            return "The Linked List is empty, no Nodes to remove"
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A Node with that data value is not present"
                else:
                    previous = current
                    current = current.get_next()

        # We don't remove anything really, we just break the link between Nodes
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())




# sll = SLL()
# print(sll.is_empty())
# node = SLLNode(5)
# sll.head = node
# print(sll.is_empty())

# sll = SLL()
# print(sll.head)
# sll.add_front('berry')
# print(sll.head)
    
# sll = SLL()
# print(sll.size())
# sll.add_front(1)
# sll.add_front(2)
# sll.add_front(3)
# print(sll.size())

# sll = SLL()
# print(sll.search(3))
# sll.add_front(1)
# sll.add_front(2)
# sll.add_front('matt')
# print(sll.search('hello'))
# print(sll.search('matt'))