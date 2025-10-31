class stock_purchase:

    def __init__(self, stock_symbol, cost_per_share, shares = 1): # must have 1 share if a purchase takes place
        self.stock_symbol = stock_symbol
        self.cost_per_share = cost_per_share
        self.shares = shares