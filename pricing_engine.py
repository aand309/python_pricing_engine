import pandas as pd

# Load product and sales data
products_df = pd.read_csv('products.csv')
sales_df = pd.read_csv('sales.csv')

# Merge the dataframes on SKU
df = pd.merge(products_df, sales_df, on='sku', how='left')
df['quantity_sold'].fillna(0, inplace=True)

# Function to apply pricing rules
def apply_pricing_rules(row):
    current_price = row['current_price']
    cost_price = row['cost_price']
    stock = row['stock']
    quantity_sold = row['quantity_sold']
    new_price = current_price

    if stock < 20 and quantity_sold > 30:
        new_price = current_price * 1.15
    elif stock > 200 and quantity_sold == 0:
        new_price = current_price * 0.7
    elif stock > 100 and quantity_sold < 20:
        new_price = current_price * 0.9

    min_price = cost_price * 1.2
    if new_price < min_price:
        new_price = min_price

    return round(new_price, 2)

# Apply rules
df['new_price'] = df.apply(apply_pricing_rules, axis=1)
df['old_price'] = df['current_price'].apply(lambda x: f"{x:.2f} USD")
df['new_price'] = df['new_price'].apply(lambda x: f"{x:.2f} USD")

# Output
output_df = df[['sku', 'old_price', 'new_price']]
output_df.to_csv('updated_prices.csv', index=False)
