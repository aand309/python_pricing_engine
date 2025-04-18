# Pricing Engine - THRD Coding Challenge

## Overview

This Python script implements a dynamic pricing engine that adjusts product prices based on inventory levels and recent sales data. The goal is to optimize product pricing in response to supply and demand while ensuring minimum profit margins.

---

## Files Included

- `pricing_engine.py`: Main Python script that processes the data and applies pricing rules.
- `updated_prices.csv`: Output file with updated product prices.
- `products.csv` and `sales.csv`: Sample input files (provided for testing).

---

## Logic & Rules Applied

Each product's price is updated according to the following priority-based rules:

1. Rule 1 – Low Stock, High Demand  
   Condition: `stock < 20` and `quantity_sold > 30`  
   Action: Increase price by 15%

2. Rule 2 – Dead Stock  
   Condition: `stock > 200` and `quantity_sold == 0`  
   Action: Decrease price by 30%

3. Rule 3 – Overstocked Inventory  
   Condition: `stock > 100` and `quantity_sold < 20`  
   Action: Decrease price by 10%

4. Rule 4 – Minimum Profit Constraint (Always Applied)  
   Ensures `new_price >= cost_price * 1.2`.  
   If not, the price is reset to `cost_price * 1.2`.

---

## How to Run

1. Ensure you have Python 3 and pandas installed:
   ```
   pip install pandas
   ```

2. Place `products.csv` and `sales.csv` in the same directory as `pricing_engine.py`.

3. Run the script:
   ```
   python pricing_engine.py
   ```

4. Check the generated output file:
   - `updated_prices.csv` containing:
     - `sku`
     - `old_price` (with "USD")
     - `new_price` (with "USD")

---

## Example Output

| sku  | old_price   | new_price   |
|------|-------------|-------------|
| A123 | 649.99 USD  | 600.00 USD  |
| B456 | 699.00 USD  | 803.85 USD  |
| C789 | 999.00 USD  | 699.30 USD  |

---

## Assumptions

- All prices are in USD.
- `quantity_sold` is assumed to be zero if not present in `sales.csv`.
- Prices are rounded to 2 decimal places.
- Only one of Rules 1–3 is applied before applying Rule 4.

---

## Author

THRD Coding Challenge — April 2025
