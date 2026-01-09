# Portfolio Rebalancing System

This project implements a **simple portfolio rebalancing system** with:
- **Backend**: FastAPI (/api)  
- **Frontend**: React component (portfolio-pie)  
- **Visualization**: Pie chart using recharts  
- **Deployment**: Vercel  

The app demonstrates how a portfolio can be tracked and rebalanced based on **stock prices**, **target allocations**, and a **total investment amount**.

---

## Dependencies

### Backend
- Python 3.x  
- FastAPI
- Uvicorn (for local development)

### Frontend
- React 18+
- Recharts

---

## API

### Base URL
```
https://portfolio-pink-nine-zqqb57t52q.vercel.app/docs
```

### Endpoints

| Method | Path             | Description |
|--------|------------------|-------------|
| GET    | `/portfolio`     | Returns the current portfolio including stock quantities, prices, and total invested value. |
| POST   | `/update_price`  | Updates the price of a stock and automatically rebalances the portfolio. Request body: `{ "key": string, "price": float }`. |
| POST   | `/restart`       | Resets the portfolio to its initial state (prices, quantities, allocations). |

---

## Frontend

### URL
```
https://portfolio-pi-iota.vercel.app/
```

### Features
- Fetches current portfolio from the backend on component mount.  
- Displays a **table** of stock quantities, prices, and share-based percentages.  
- Displays a **pie chart** showing the **share distribution** (100% = total number of shares).  
- Simple form to **update stock price** and automatically rebalance.  
- Button to **restart portfolio** to initial state.

---

## Logic & Assumptions

### 1. Total Investment
Portfolio is initialized with a fixed total investment amount.

### 2. Target Allocation
Each stock has a target percentage allocation of the total investment.

### 3. Initial Quantities
Calculated as:
```python
quantity = (target_allocation * total_invest) / stock_price
```

### 4. Price Updates
When a stock price changes:
- Portfolio value is recalculated (`calculate_total_invested()`)
- New target quantities are computed (`rebalance()`)
- Difference determines shares to buy/sell

### 5. Share-based Percentages
Pie chart reflects percentage of shares, not value or target allocation:
```python
% of shares = stock_quantity / total_quantity
```

### Assumptions
- Quantities can be fractional for simplicity
- Portfolio rebalancing occurs automatically on price update
- All operations are in-memory, no database is used

---

## Folder Structure
```
root/
├── api/                     # FastAPI backend
│   ├── main.py
│   └── portfolio.py
└── portfolio-pie/           # React frontend
    └── Portfolio.jsx
```

---

## Development

### Backend (FastAPI)
```bash
cd api
pip install fastapi uvicorn
uvicorn main:app --reload
```

### Frontend (React)
```bash
cd portfolio-pie
npm install
npm start
```

---

## Deployment

- **Backend** deployed to Vercel at: `https://portfolio-pink-nine-zqqb57t52q.vercel.app`
- **Frontend** deployed to Vercel at: `https://portfolio-pi-iota.vercel.app/`

---

## Notes

- The app demonstrates portfolio rebalancing logic and dynamic visualization.
- Designed for educational or demo purposes.
- No persistence; all data is in-memory.

---

## Prompts & AI Assistance

This project was partially developed using ChatGPT for basic FastAPI endpoints and frontend logic.

**Prompt session**: [https://chatgpt.com/g/g-p-69613d837d348191a78d8c6ddf5631d6-fintual/project](https://chatgpt.com/g/g-p-69613d837d348191a78d8c6ddf5631d6-fintual/project)

---