from ledger_entry import ledger_entry
from stock_purchase import stock_purchase

class stock_ledger: # list of linked deques

    def __init__(self):
        self.list_of_linked_deques = []
    
    def buy(self, stock_symbol, shares_bought, price_per_share):
        entry = self.get_entry(stock_symbol) # check for any existing ledger entries for the stock being purchased
        if not entry: # if get entry returns none then we must create a new ledger entry for the stock being purchased
            entry = ledger_entry(stock_symbol)
            self.list_of_linked_deques.append(entry)
        for shares_number in range(shares_bought): # adds a ledger entry for each share bought
            entry.add_purchase(stock_purchase(stock_symbol, price_per_share))

    def sell(self, stock_symbol, shares_sold, price_per_share):
        entry = self.get_entry(stock_symbol)
        if not entry:
            print(f"You do not own any {stock_symbol} shares.")
        # complete ledger_entry remove_purchase


    def display_ledger(self):
        if not self.list_of_linked_deques:
            print("Stock Ledger empty.")
            return None
        for entry in self.list_of_linked_deques:
            entry.display_entry()
            print()

    #def contains(self, stock_symbol):


    def get_entry(self, stock_symbol):
        for entry in self.list_of_linked_deques: # loop through current ledger entries
            if entry.stock_symbol == stock_symbol:
                return entry
        return None
    