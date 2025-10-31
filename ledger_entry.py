from linked_deque import linked_deque

class ledger_entry:

    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.new_stock_purchases = linked_deque()

    def add_purchase(self, new_purchase):
        self.new_stock_purchases.add_to_back(new_purchase)

    def remove_purchase(self): # complete linked deque remove_front()
        pass

    def equals(self, other):
        return self.stock_symbol == other.stock_symbol

    def display_entry(self):
        print(f"{self.stock_symbol}:")
        self.new_stock_purchases.display()
    