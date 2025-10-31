class linked_deque:

    def __init__(self):
        self.front = None
        self.back = None
    
    def add_to_back(self, new_entry):
        new_node = self.DLNode(self.back, new_entry, None)
        if self.is_empty():
            self.front = new_node
        else:
            self.back.set_next_node(new_node)
        self.back = new_node
    
    def add_to_front(self, new_entry):
        new_node = self.DLNode(None, new_entry, self.front)
        if self.is_empty(): # checks if this is the first purchase entry
            self.back = new_node
        else:
            self.front.set_previous_node(new_node)
        self.front = new_node
    
    def get_back(self):
        if self.back:
            return self.back.get_data()
    
    def get_front(self):
        if self.front:
            return self.front.get_data()
    
    def remove_front(self):
        if self.is_empty():
            return None
        removed = self.front.get_data() # make a temp for this
        self.front = self.front.get_next_node() # change the deque
        if self.front: # check if empty
            self.front.set_previous_node(None)
        else: # only one node in the deque now deque will be empty
            self.back = None
        return removed

    def remove_back(self):
        if self.is_empty():
            return None
        removed = self.back.get_data()
        self.back = self.back.get_previous_node()
        if self.back:
            self.back.set_next_node(None)
        else:
            self.front = None
        return removed
    
    def clear(self):
        self.front = None
        self.back = None

    def is_empty(self):
        return self.front is None
    
    def display(self):
        current = self.front
        while current: # loop while a next node exists and prints the deque
            data = current.get_data()
            print(f"  {data.stock_symbol}: ${data.cost_per_share:.2f} per share ({data.shares} shares)")
            current = current.get_next_node()
        
    
    class DLNode:

        def __init__(self, previous_node = None, data_portion = None, next_node = None):
            self.data_portion = data_portion
            self.previous_node = previous_node
            self.next_node = next_node
    
        def get_data(self):
            return self.data_portion

        def set_data(self, new_data):
            self.data_portion = new_data
        
        def get_next_node(self):
            return self.next_node
        
        def set_next_node(self, next_node):
            self.next_node = next_node
        
        def get_previous_node(self):
            return self.previous_node
        
        def set_previous_node(self, previous_node):
            self.previous_node = previous_node
    