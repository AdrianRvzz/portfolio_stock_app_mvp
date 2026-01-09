# Portfolio Rebalancing Notes

## Concepts

- **Stock**: Represents a minimal part of a company.  
  - Attributes: \`key\` (ticker), \`price\`.  
  - Methods: \`update_price(last_available_price)\`.

- **Portfolio**: Holds multiple stocks and a target allocation.  
  - Attributes: list of stocks with quantity and target allocation, total invested.  
  - Methods:
    - \`calculate_total_invested()\`: Computes current total value of the portfolio.  
    - \`rebalance()\`: Adjusts stock quantities to match target allocation based on current prices.

## Example

1. Initial investment: \$10,000  
2. Target allocation: Apple 60%, Meta 40%  
3. Stock prices: Apple \$25, Meta \$40  

**Initial quantities**:  
- Apple: 10,000 * 0.6 / 25 = 240 shares  
- Meta: 10,000 * 0.4 / 40 = 100 shares  

**After price changes**:  
- Apple \$20, Meta \$42 → total portfolio value: \$9,000  
- New distribution:
  - Apple ≈ 53.3%  
  - Meta ≈ 46.7%  

**Rebalance target quantities**:  
- Apple: 9,000 * 0.6 / 20 = 270 shares → buy 30 shares  
- Meta: 9,000 * 0.4 / 42 ≈ 85.7 shares → sell 14.3 shares  

## Data Structure

- \`invests\` list:  
\`\`\`python
invests = [
    {"stock": Stock, "allocation": float},
]
\`\`\`
- Each position tracks: stock, quantity, allocation.

## Workflow

1. Create Stock instances.  
2. Initialize Portfolio with investments and total amount.  
3. Update stock prices with \`update_price()\`.  
4. Call \`rebalance()\` to adjust quantities.  
5. Use \`calculate_total_invested()\` to track portfolio value.