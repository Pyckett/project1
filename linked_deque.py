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
    
    #def remove_front(self):
        

    #def remove_back(self):

    
    def clear(self):
        self.front = None
        self.back = None

    def is_empty(self):
        return self.front is None
    
    def display(self):
        if self.is_empty(): # check if empty
            print("Stock Ledger empty.")
            return None
        current_node = self.front # start at front
        purchase = current_node.get_data() # get front node data
        while current_node is not None:
            print(f"  {purchase.stock_symbol} Share/s - Bought at ${purchase.cost_per_share}")
            current_node = current_node.get_next_node()
        
    
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
    