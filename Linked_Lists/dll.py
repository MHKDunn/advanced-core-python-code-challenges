class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return f"<DLLNode object: data={self.data}, type={type(self.data)}>"

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
        Replace existing value of self.next with new_next parameter
        """
        self.next = new_next

    def get_previous(self):
        """
        Return the attribute self.previous
        """
        return self.previous
    
    def set_previous(self, new_previous):
        """ 
        Replace existing value of self.previous with new_previous parameter
        """
        self.previous = new_previous
    


# node1 = DLLNode(1)
# node2 = DLLNode(2)

# print(node1.get_previous())
# node1.set_previous(node2)
# print(node1.get_previous())
# # node.set_next(new_node)
# # print(node.get_next())
        

class DLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"<DLL object: head=>{self.head}"
    
    def isempty(self):
        return self.head is None
    
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

    def add_front(self, new_data):
        """ 
        Add node whose data is the new_data argument to the front of the Linked List
        """

        temp = DLLNode(new_data)
        temp.set_next(self.head)
        if self.head is not None:
            self.head.set_previous(temp)

        self.head = temp

    def remove(self, data):
        """ 
        Removes the first occurrence of a Node that contains the data 
        argument as its self.data attribute.
        Returns Nothing
        
        The time complexity is 0(n) because in the worst case, we have to visit every 
        Node before finding the one we want to remove
        """

        if self.head is None:
            return "Linked List is empty, no Nodes to remove"
        
        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A Node with that data value is not present"
                else:
                    current = current.get_next()

        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())
                

    

