from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from stock_portfolio_module import Stock, Portfolio 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "https://portfolio-pi-iota.vercel.app",  
    "http://localhost:3000",          
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=False,      
    allow_methods=["*"],          
    allow_headers=["*"],         
)

# ----- Initialize in-memory portfolio -----
def create_portfolio():
    apple_stock = Stock("AAPL", 25)
    meta_stock = Stock("META", 40)
    google_stock = Stock("GOOG", 120)
    amazon_stock = Stock("AMZN", 150)
    microsoft_stock = Stock("MSFT", 300)

    invests = [
        {"stock": apple_stock, "allocation": 0.2},
        {"stock": meta_stock, "allocation": 0.2},
        {"stock": google_stock, "allocation": 0.2},
        {"stock": amazon_stock, "allocation": 0.2},
        {"stock": microsoft_stock, "allocation": 0.2},
    ]

    return Portfolio(invests, total_invest=10000)
portfolio = create_portfolio()
# ----- Request model -----
class PriceUpdate(BaseModel):
    key: str
    price: float

# ----- API endpoints -----
@app.get("/portfolio")
def get_portfolio():
    """Return current portfolio state."""
    return portfolio.to_dict()

@app.post("/update_price")
def update_price(data: PriceUpdate):
    """Update stock price and rebalance portfolio."""
    # Find stock
    found = False
    for pos in portfolio.allocations:
        if pos["stock"].key == data.key:
            pos["stock"].update_price(data.price)
            found = True
            break
    if not found:
        raise HTTPException(status_code=404, detail="Stock not found")
    
    # Rebalance automatically
    portfolio.rebalance()
    return portfolio.to_dict()

@app.post("/restart")
def restart_portfolio():
    """Reset portfolio to initial state."""
    global portfolio
    portfolio = create_portfolio()
    return portfolio.to_dict()