class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

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
    


node1 = DLLNode(1)
node2 = DLLNode(2)

print(node1.get_previous())
node1.set_previous(node2)
print(node1.get_previous())
# node.set_next(new_node)
# print(node.get_next())

