from linked_deque import linked_deque

class ledger_entry:

    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.new_stock_purchases = linked_deque()

    def add_purchase(self, new_purchase):
        self.new_stock_purchases.add_to_back(new_purchase)

    def remove_purchase(self):
        return self.new_stock_purchases.remove_front()

    def equals(self, other):
        return self.stock_symbol == other.stock_symbol

    def display_entry(self):
        print(f"{self.stock_symbol}: ", end="")
        if self.new_stock_purchases.is_empty(): # check for existing shares
            print("No shares")
            return
        current = self.new_stock_purchases.front # declare a current front value
        first = True
        while current: # create a loop as long as we have values
            purchase = current.get_data()
            if not first:
                print(", ", end="")
            print(f"{purchase.cost_per_share:.1f} ({purchase.shares} shares)", end="") # get the current entry data and print
            current = current.get_next_node() # redeclare current as next
            first = False
        print()
    