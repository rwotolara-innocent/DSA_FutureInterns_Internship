<<<<<<< HEAD
# Import necessary libraries 
import pandas as pd  # Import pandas library for data manipulation and analysis
from google.colab import drive  # Import drive module to access Google Drive from Colab

# Mount Google Drive
drive.mount('/content/drive')  # Connect Google Drive to the Colab environment for file access

# Load CSV files
orders = pd.read_csv('olist_orders_dataset.csv')  # Load orders dataset into a DataFrame
order_items = pd.read_csv('olist_order_items_dataset.csv')  # Load order items dataset into a DataFrame
products = pd.read_csv('olist_products_dataset.csv')  # Load products dataset into a DataFrame

# Merge data
merged_data = pd.merge(orders, order_items, on='order_id')  # Combine orders and order_items tables using order_id as the key
merged_data = pd.merge(merged_data, products, on='product_id')  # Add product information to the merged data using product_id as the key

# Handle missing values
merged_data = merged_data.dropna(subset=['product_category_name', 'price', 'order_purchase_timestamp']).copy()  # Remove rows where essential columns have missing values and create independent copy

# Convert date column
merged_data['order_purchase_timestamp'] = pd.to_datetime(merged_data['order_purchase_timestamp'])  # Convert timestamp column from string to datetime format for date operations

# Calculate total sales per product (with product name)
sales_per_product = (merged_data.groupby(['product_id', 'product_category_name'])['price']  # Group data by product_id and category, then sum prices
                    .sum()  # Sum all prices for each product
                    .reset_index()  # Convert grouped data back to regular DataFrame format
                    .rename(columns={'price': 'total_sales', 'product_category_name': 'product_name'}))  # Rename columns for clarity

# Calculate total sales per category
sales_per_category = (merged_data.groupby('product_category_name')['price']  # Group data by product category
                     .sum()  # Sum all prices for each category
                     .reset_index()  # Convert grouped data back to regular DataFrame format
                     .rename(columns={'price': 'category_revenue'}))  # Rename price column to category_revenue

# Calculate monthly sales trend
merged_data['month'] = merged_data['order_purchase_timestamp'].dt.to_period('M')  # Extract month-year from timestamp and create new column
sales_trend = (merged_data.groupby('month')['price']  # Group data by month
              .sum()  # Sum all prices for each month
              .reset_index()  # Convert grouped data back to regular DataFrame format
              .rename(columns={'price': 'monthly_sales'}))  # Rename price column to monthly_sales

# Export to CSV
sales_per_product[['product_name', 'total_sales']].to_csv('/content/drive/MyDrive/sales_per_product.csv', index=False)  # Save product sales data to CSV file in Google Drive
sales_per_category.to_csv('/content/drive/MyDrive/sales_per_category.csv', index=False)  # Save category sales data to CSV file in Google Drive
sales_trend.to_csv('/content/drive/MyDrive/sales_trend.csv', index=False)  # Save monthly sales trend data to CSV file in Google Drive

print("Files saved successfully to Google Drive!")  # Display success message when all files are saved
=======
# Import necessary libraries 
import pandas as pd  # Import pandas library for data manipulation and analysis
from google.colab import drive  # Import drive module to access Google Drive from Colab

# Mount Google Drive
drive.mount('/content/drive')  # Connect Google Drive to the Colab environment for file access

# Load CSV files
orders = pd.read_csv('olist_orders_dataset.csv')  # Load orders dataset into a DataFrame
order_items = pd.read_csv('olist_order_items_dataset.csv')  # Load order items dataset into a DataFrame
products = pd.read_csv('olist_products_dataset.csv')  # Load products dataset into a DataFrame

# Merge data
merged_data = pd.merge(orders, order_items, on='order_id')  # Combine orders and order_items tables using order_id as the key
merged_data = pd.merge(merged_data, products, on='product_id')  # Add product information to the merged data using product_id as the key

# Handle missing values
merged_data = merged_data.dropna(subset=['product_category_name', 'price', 'order_purchase_timestamp']).copy()  # Remove rows where essential columns have missing values and create independent copy

# Convert date column
merged_data['order_purchase_timestamp'] = pd.to_datetime(merged_data['order_purchase_timestamp'])  # Convert timestamp column from string to datetime format for date operations

# Calculate total sales per product (with product name)
sales_per_product = (merged_data.groupby(['product_id', 'product_category_name'])['price']  # Group data by product_id and category, then sum prices
                    .sum()  # Sum all prices for each product
                    .reset_index()  # Convert grouped data back to regular DataFrame format
                    .rename(columns={'price': 'total_sales', 'product_category_name': 'product_name'}))  # Rename columns for clarity

# Calculate total sales per category
sales_per_category = (merged_data.groupby('product_category_name')['price']  # Group data by product category
                     .sum()  # Sum all prices for each category
                     .reset_index()  # Convert grouped data back to regular DataFrame format
                     .rename(columns={'price': 'category_revenue'}))  # Rename price column to category_revenue

# Calculate monthly sales trend
merged_data['month'] = merged_data['order_purchase_timestamp'].dt.to_period('M')  # Extract month-year from timestamp and create new column
sales_trend = (merged_data.groupby('month')['price']  # Group data by month
              .sum()  # Sum all prices for each month
              .reset_index()  # Convert grouped data back to regular DataFrame format
              .rename(columns={'price': 'monthly_sales'}))  # Rename price column to monthly_sales

# Export to CSV
sales_per_product[['product_name', 'total_sales']].to_csv('/content/drive/MyDrive/sales_per_product.csv', index=False)  # Save product sales data to CSV file in Google Drive
sales_per_category.to_csv('/content/drive/MyDrive/sales_per_category.csv', index=False)  # Save category sales data to CSV file in Google Drive
sales_trend.to_csv('/content/drive/MyDrive/sales_trend.csv', index=False)  # Save monthly sales trend data to CSV file in Google Drive

print("Files saved successfully to Google Drive!")  # Display success message when all files are saved
>>>>>>> 1811ae7f135f4abe5cfc3b187405e5075358379b
