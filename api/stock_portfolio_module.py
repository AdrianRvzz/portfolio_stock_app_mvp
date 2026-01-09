

class Stock:
    def __init__(self, key: str, price: float):
        #Ticker o symbol of the stock such Apple -> AAPL

        """
        Stock represents a minimal part of a company
        :param key: Ticker or stock symbol, ej. "AAPL"
        :param price: Actual price
        """
        self.key = key
        self.price = price
        return
    def update_price(self, last_available_price):
        self.price = last_available_price
        return
    
    def __str__(self):
        return f"Stock {self.key}, Price: {self.price}"
    
class Portfolio:

    def __init__(self, invests, total_invest):
        #We assume that we can compute the distribution by the quantity of each stock / them
        #For instance, Stock("META", 10, 40) and Stock("APPL",10, 60 )
        #This accomplish the example 40% Meta, 60% APPL if we invest 400 in META and
        #600 in apple we got a distribution of 40% and 60%

        self.allocations = []
        self.total_invest = total_invest
       
        for pos in invests:
            stock = pos["stock"]
            allocation = pos["allocation"]
            quantity = (allocation * self.total_invest) / stock.price  
            self.allocations.append({
                "stock": stock,
                "quantity": quantity,
                "allocation": allocation
            })
            
    def calculate_total_invested(self):
        return sum(pos["stock"].price * pos["quantity"] for pos in self.allocations)
            
    def rebalance(self):
        self.total_invest = self.calculate_total_invested()
        total = self.total_invest
        for pos in self.allocations:
            target_value = pos["allocation"] * total
            target_quantity = target_value / pos["stock"].price
            diff = target_quantity - pos["quantity"]

            pos["quantity"] += diff

        return
    def to_dict(self):
        """Return portfolio as dict for API response."""
        return {
            "total_value": self.calculate_total_invested(),
            "invests": {
                pos["stock"].key: {
                    "allocation": pos["allocation"],
                    "quantity": pos["quantity"],
                    "price": pos["stock"].price
                } for pos in self.allocations
            }
        }
    def __str__(self):
        
        lines = [f"Inversion {self.total_invest} " ]
        for pos in self.allocations:
            stock = pos["stock"]
            qty = pos["quantity"]
            alloc = pos["allocation"]
            lines.append(f"{stock.key}: Quantity={qty:.2f}, Allocation={alloc*100:.1f}%")
        return "\n".join(lines)
        
apple_stock = Stock("AAPL", 25)
meta_stock = Stock("META", 40)

invests = [
    {"stock": apple_stock, "allocation": 0.6},
    {"stock": meta_stock, "allocation": 0.4}
]

total_invested = 10000

myPortfolio = Portfolio(invests, total_invested)
print(myPortfolio)
apple_stock.update_price(50)
meta_stock.update_price(1000)

myPortfolio.rebalance()
print(myPortfolio)


#
