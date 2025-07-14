import pandas as pd  # Import pandas library for data manipulation
from google.colab import drive  # Import drive module to access Google Drive

# Mount Google Drive to access files and save outputs
drive.mount('/content/drive')

# Load CSV files into DataFrames
orders = pd.read_csv('olist_orders_dataset.csv')  # Load orders data
order_items = pd.read_csv('olist_order_items_dataset.csv')  # Load order items data
products = pd.read_csv('olist_products_dataset.csv')  # Load products data

# Merge orders and order_items on order_id
merged_data = pd.merge(orders, order_items, on='order_id')  # Join orders with order items using order_id as key

# Merge with products on product_id
merged_data = pd.merge(merged_data, products, on='product_id')  # Join result with products using product_id as key

# Handle missing values - use proper inplace assignment
merged_data = merged_data.fillna({'product_category_name': 'Unknown'})  # Fill missing category names with 'Unknown'
merged_data = merged_data.dropna(subset=['price', 'order_purchase_timestamp'])  # Remove rows with missing price or timestamp

# Convert date column to datetime
merged_data['order_purchase_timestamp'] = pd.to_datetime(merged_data['order_purchase_timestamp'])  # Convert timestamp to datetime format

# Calculate total sales per product
sales_per_product = (merged_data.groupby('product_id')['price']  # Group by product_id and select price column
                    .sum()  # Sum prices for each product
                    .reset_index()  # Reset index to make product_id a column
                    .rename(columns={'price': 'total_sales'}))  # Rename price column to total_sales

# Calculate total sales per category
sales_per_category = (merged_data.groupby('product_category_name')['price']  # Group by category and select price column
                     .sum()  # Sum prices for each category
                     .reset_index()  # Reset index to make category a column
                     .rename(columns={'price': 'category_revenue'}))  # Rename price column to category_revenue

# Calculate monthly sales trend
merged_data['month'] = merged_data['order_purchase_timestamp'].dt.to_period('M')  # Extract month-year from timestamp
sales_trend = (merged_data.groupby('month')['price']  # Group by month and select price column
              .sum()  # Sum prices for each month
              .reset_index()  # Reset index to make month a column
              .rename(columns={'price': 'monthly_sales'}))  # Rename price column to monthly_sales

# Export to CSV files in Google Drive
sales_per_product.to_csv('/content/drive/MyDrive/sales_per_product.csv', index=False)  # Save product sales data to Drive
sales_per_category.to_csv('/content/drive/MyDrive/sales_per_category.csv', index=False)  # Save category sales data to Drive
sales_trend.to_csv('/content/drive/MyDrive/sales_trend.csv', index=False)  # Save monthly sales trend to Drive

print("Files saved successfully to Google Drive!")  # Confirmation message
