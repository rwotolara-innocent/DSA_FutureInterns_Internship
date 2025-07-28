# Import necessary libraries
import pandas as pd  # Import pandas library for data manipulation and analysis
import matplotlib.pyplot as plt  # Import matplotlib for creating visualizations
import seaborn as sns  # Import seaborn for enhanced visualizations
import plotly.express as px  # Import plotly for interactive visualizations
from google.colab import files  # Import files module to download files in Colab
from google.colab import drive  # Import drive module to access Google Drive from Colab

# Mount Google Drive
drive.mount('/content/drive')  # Connect Google Drive to the Colab environment for file access

# Load CSV file
df = pd.read_csv('marketing_data.csv')  # Load Kaggle Marketing Campaign dataset into a DataFrame

# Clean the data
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')  # Convert Dt_Customer to datetime with specific format
df['Income'] = df['Income'].replace('[\$,]', '', regex=True)  # Remove dollar signs and commas from Income
df['Income'] = pd.to_numeric(df['Income'], errors='coerce')  # Convert Income to numeric, coerce errors to NaN
df['Income'] = df['Income'].fillna(df['Income'].mean())  # Fill missing Income values with mean of non-missing values
df.drop_duplicates(inplace=True)  # Remove duplicate rows
df.drop(['Z_CostContact', 'Z_Revenue'], axis=1, inplace=True, errors='ignore')  # Drop unnecessary columns
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns  # Select numeric columns for later use
print("Missing values after cleaning:")  # Display missing values summary
print(df.isnull().sum())  # Print count of missing values per column
print("Data types after cleaning:")  # Display data types summary
print(df.dtypes)  # Print data types of all columns

# Calculate key metrics
df['Total_Acceptances'] = df[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'Response']].sum(axis=1)  # Sum campaign acceptances per customer
df['Exposures'] = 6  # Assume 6 campaign exposures per customer
df['Acceptance Rate'] = (df['Total_Acceptances'] / df['Exposures']) * 100  # Calculate Acceptance Rate as (acceptances/exposures) * 100
cost_per_exposure = 5  # Set cost per exposure to $5
df['Estimated_Cost'] = df['Exposures'] * cost_per_exposure  # Calculate estimated cost as exposures * cost_per_exposure
df['Total_Purchases'] = df['NumWebPurchases'] + df['NumCatalogPurchases'] + df['NumStorePurchases']  # Sum total purchases across channels
df['Revenue'] = df[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)  # Sum revenue from product categories
df['CPP'] = df['Estimated_Cost'] / df['Total_Purchases']  # Calculate Cost Per Purchase as cost/total purchases
df['ROI'] = ((df['Revenue'] - df['Estimated_Cost']) / df['Estimated_Cost']) * 100  # Calculate ROI as ((revenue - cost) / cost) * 100
df[numeric_cols] = df[numeric_cols].fillna(0)  # Fill missing values in numeric columns with 0
df[numeric_cols] = df[numeric_cols].replace([float('inf'), -float('inf')], 0)  # Replace infinities with 0

# Summarize campaign performance
campaigns = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'Response']  # Define campaign columns
power_bi_data = df.groupby('Education').agg({  # Group data by Education for segmentation analysis
    'Acceptance Rate': 'mean',  # Calculate average Acceptance Rate
    'ROI': 'mean',  # Calculate average ROI
    'Total_Purchases': 'sum',  # Sum total purchases
    'Revenue': 'sum',  # Sum total revenue
    'Estimated_Cost': 'sum'  # Sum total estimated cost
}).round(2).reset_index()  # Round to 2 decimal places and convert to DataFrame
print("Summarized data for Power BI:")  # Display summarized data
print(power_bi_data)  # Print summarized DataFrame

# Generate visualizations
# Visualization 1: Acceptance Rate by Campaign
acceptance_rates = [df[camp].mean() * 100 for camp in campaigns]  # Calculate acceptance rates for each campaign
plt.figure(figsize=(10, 6))  # Set figure size
sns.barplot(x=campaigns, y=acceptance_rates)  # Create bar plot
plt.title('Acceptance Rate by Campaign')  # Set plot title
plt.xlabel('Campaign')  # Set x-axis label
plt.ylabel('Acceptance Rate (%)')  # Set y-axis label
plt.xticks(rotation=45)  # Rotate x-axis labels
plt.tight_layout()  # Adjust layout
plt.savefig('/content/drive/MyDrive/acceptance_rate_plot.png')  # Save plot to Google Drive
plt.close()  # Close plot

# Visualization 2: Average Purchases by Channel
purchase_channels = ['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']  # Define purchase channel columns
avg_purchases = [df[channel].mean() for channel in purchase_channels]  # Calculate average purchases per channel
plt.figure(figsize=(10, 6))  # Set figure size
sns.barplot(x=purchase_channels, y=avg_purchases)  # Create bar plot
plt.title('Average Purchases by Channel')  # Set plot title
plt.xlabel('Purchase Channel')  # Set x-axis label
plt.ylabel('Average Purchases')  # Set y-axis label
plt.xticks([0, 1, 2], ['Web', 'Catalog', 'Store'])  # Customize x-axis labels
plt.tight_layout()  # Adjust layout
plt.savefig('/content/drive/MyDrive/purchases_by_channel_plot.png')  # Save plot to Google Drive
plt.close()  # Close plot

# Visualization 3: Income vs. Revenue by Campaign Acceptance
fig = px.scatter(df, x='Income', y='Revenue', color='Total_Acceptances', size='Total_Purchases',
                 hover_data=['Education', 'Marital_Status'], title='Income vs. Revenue by Campaign Acceptance')  # Create interactive scatter plot
fig.update_layout(xaxis_title='Income ($)', yaxis_title='Revenue ($)')  # Set axis labels
fig.write_html('/content/drive/MyDrive/income_vs_revenue.html')  # Save interactive plot to Google Drive

# Visualization 4: Revenue Distribution by Product
product_cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']  # Define product columns
product_sums = [df[col].sum() for col in product_cols]  # Sum revenue for each product category
plt.figure(figsize=(8, 8))  # Set figure size
plt.pie(product_sums, labels=product_cols, autopct='%1.1f%%', startangle=140,
        colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])  # Create pie chart
plt.title('Revenue Distribution by Product Category')  # Set plot title
plt.tight_layout()  # Adjust layout
plt.savefig('/content/drive/MyDrive/revenue_by_product_plot.png')  # Save plot to Google Drive
plt.close()  # Close plot

# Analyze and provide insights
print("Campaign Performance Insights:")  # Display campaign performance header
for camp in campaigns:  # Loop through campaigns
    rate = df[camp].mean() * 100  # Calculate acceptance rate
    print(f"{camp}: Acceptance Rate = {rate:.2f}%")  # Print acceptance rate
avg_income = df['Income'].mean()  # Calculate average income
print(f"Average Customer Income: ${avg_income:.2f}")  # Print average income
top_country = df['Country'].value_counts().idxmax()  # Find most common country
print(f"Most Common Country: {top_country}")  # Print top country
top_education = df['Education'].value_counts().idxmax()  # Find most common education
print(f"Most Common Education: {top_education}")  # Print top education
top_marital = df['Marital_Status'].value_counts().idxmax()  # Find most common marital status
print(f"Most Common Marital Status: {top_marital}")  # Print top marital status

# Export to CSV
df.to_csv('/content/drive/MyDrive/processed_campaign_data.csv', index=False)  # Save processed data to CSV file in Google Drive
power_bi_data.to_csv('/content/drive/MyDrive/power_bi_summary_data.csv', index=False)  # Save summarized data to CSV file in Google Drive

# Download files for local backup
files.download('/content/drive/MyDrive/processed_campaign_data.csv')  # Download processed data
files.download('/content/drive/MyDrive/power_bi_summary_data.csv')  # Download summarized data
files.download('/content/drive/MyDrive/acceptance_rate_plot.png')  # Download acceptance rate plot
files.download('/content/drive/MyDrive/purchases_by_channel_plot.png')  # Download purchases by channel plot
files.download('/content/drive/MyDrive/revenue_by_product_plot.png')  # Download revenue by product plot
files.download('/content/drive/MyDrive/income_vs_revenue.html')  # Download interactive scatter plot

# Display success message
print("Files saved successfully to Google Drive!")  # Confirm file save operation
