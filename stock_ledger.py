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
        entry.add_purchase(stock_purchase(stock_symbol, price_per_share, shares_bought))

    def sell(self, stock_symbol, shares_sold, price_per_share):
        entry = self.get_entry(stock_symbol) # check for any existing ledger entries for the stock being sold
        if not entry:
            print(f"You do not own any {stock_symbol} shares.")
            return None
        remaining_to_sell = shares_sold
        while remaining_to_sell > 0 and not entry.new_stock_purchases.is_empty(): # create a loop to run for how many shares sold
            front_purchase = entry.new_stock_purchases.get_front() # declare a current front value in the ledger
            if front_purchase.shares <= remaining_to_sell:
                remaining_to_sell -= front_purchase.shares
                entry.new_stock_purchases.remove_front() # if we still have shares to sell this is where we remove the shares
            else:
                front_purchase.shares -= remaining_to_sell
                remaining_to_sell = 0

    def display_ledger(self):
        print("---- Stock Ledger ----")
        if not self.list_of_linked_deques:
            print("Stock Ledger empty.")
            return
        for entry in self.list_of_linked_deques:
            entry.display_entry()
        print()

    def contains(self, stock_symbol):
        return self.get_entry(stock_symbol) is not None

    def get_entry(self, stock_symbol):
        for entry in self.list_of_linked_deques: # loop through current ledger entries
            if entry.stock_symbol == stock_symbol:
                return entry
        return None
    