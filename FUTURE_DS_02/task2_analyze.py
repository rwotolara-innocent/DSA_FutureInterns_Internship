# Import necessary libraries
import pandas as pd  # Import pandas library for data manipulation and analysis
from google.colab import drive  # Import drive module to access Google Drive from Colab

# Mount Google Drive
drive.mount('/content/drive')  # Connect Google Drive to the Colab environment for file access

# Load CSV file
df = pd.read_csv('/content/drive/MyDrive/facebook_ad_campaign.csv')  # Load Facebook ad campaign dataset into a DataFrame

# Auto-detect column names
def get_column(keywords):  # Define function to find column names based on keywords
    for keyword in keywords:
        for col in df.columns:
            if keyword.lower() in col.lower():
                return col
    return df.columns[0] if len(df.columns) > 0 else None  # Return first column if no match found

# Identify required columns
impressions = get_column(['impression']) or get_column(['reach', 'views'])  # Find impressions column with fallback
clicks = get_column(['click']) or get_column(['engagement', 'interaction'])  # Find clicks column with fallback
conversions = get_column(['conversion']) or get_column(['result', 'action'])  # Find conversions column with fallback
spend = get_column(['spend', 'spent', 'cost']) or get_column(['budget', 'amount'])  # Find spend column with fallback
campaign = get_column(['campaign']) or get_column(['ad_set', 'group', 'name'])  # Find campaign column with fallback

# Calculate Click-Through Rate (CTR)
df['CTR'] = (df[clicks] / df[impressions]) * 100  # Calculate CTR as (clicks/impressions) * 100

# Calculate Return on Investment (ROI)
avg_conversion_value = 50  # Set average conversion value to $50
df['ROI'] = ((df[conversions] * avg_conversion_value - df[spend]) / df[spend]) * 100  # Calculate ROI as ((conversions * value - spend) / spend) * 100

# Summarize campaign performance
power_bi_data = df.groupby(campaign).agg({  # Group data by campaign
    'CTR': 'mean',  # Calculate average CTR
    'ROI': 'mean',  # Calculate average ROI
    clicks: 'sum',  # Sum total clicks
    impressions: 'sum',  # Sum total impressions
    conversions: 'sum',  # Sum total conversions
    spend: 'sum'  # Sum total spend
}).round(2).reset_index()  # Round to 2 decimal places and convert to DataFrame

# Export to CSV
power_bi_data.to_csv('/content/drive/MyDrive/facebook_powerbi_data.csv', index=False)  # Save summarized data to CSV file in Google Drive

# Display success message
print("File saved successfully to Google Drive!")  # Confirm file save operation
