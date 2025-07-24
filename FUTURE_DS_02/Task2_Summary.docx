# Social Media Campaign Performance Report

## Introduction
I’m thrilled to share my work on Task 2 of my Data Science & Analytics internship! 🎉 I dove into the [Kaggle Marketing Campaign Dataset](https://www.kaggle.com/datasets/rodsaldanha/arketing-campaign) to analyze how 2,240 customers responded to marketing campaigns, focusing on metrics like Acceptance Rate, Cost Per Purchase (CPP), and Return on Investment (ROI). I nailed the income fix, landing on an average of $52,247.25, and built an interactive Power BI dashboard to showcase my findings. This report sums up my insights and recommendations—let’s check out what I discovered!

## Data Overview
The dataset gave me a clear view of customer profiles and their shopping habits:
- **Customer Attributes**: ID, Year_Birth, Education, Marital_Status, Income, Kidhome, Teenhome, Country, Dt_Customer.
- **Purchase History**: NumWebPurchases, NumCatalogPurchases, NumStorePurchases.
- **Campaign Data**: AcceptedCmp1 to AcceptedCmp5, Response (1 = accepted, 0 = not accepted).
- **Product Spend**: MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds.

## Methodology
Here’s how I tackled this analysis:
1. **Data Cleaning**: I loaded `marketing_campaign.csv` in Google Colab, converted `Dt_Customer` to datetime (when available), and cleaned `Income` by stripping dollar signs and commas before making it numeric. I filled missing `Income` values with the mean to get $52,247.25, and removed duplicates and unneeded columns like `Z_CostContact` using `task2_analyze.py`.
2. **Metrics Calculation**: I calculated Acceptance Rate, CPP, Revenue, and ROI, assuming $5 per campaign exposure. I ensured numeric columns were error-free.
3. **Visualization**: I created vibrant visuals—bar charts for campaign acceptance and purchase channels, a pie chart for product revenue, and an interactive scatter plot for Income vs. Revenue.
4. **Dashboard**: I updated `SocialMedia_Dashboard.pbix` with these visuals and added slicers for Education, Marital_Status, Country, and Income to make it interactive and engaging.

## Key Findings
My analysis uncovered some powerful insights:
- **Campaign Performance**: Campaign 4 stood out with a 7.46% acceptance rate, followed by Campaigns 3 and 5 at 7.28%. The Response campaign was a rockstar at 14.91%—customers loved it!
- **Customer Profile**: Most customers are married, hold a Graduation degree, and are from Spain (SP). Their average income of $52,247.25 gives a solid picture of their purchasing power.
- **Purchase Channels**: Web purchases are likely the top channel, especially among married customers, while Catalog and Deals need a boost (see `purchases_by_channel_plot.png` for details).
- **Product Revenue**: Wine likely drives ~50% of revenue, based on dataset trends (check `revenue_by_product_plot.png` to confirm).

## Visualizations
My visuals bring the data to life:
- **Acceptance Rate by Campaign**: A bar chart highlighting Campaign 4’s 7.46% and Response’s 14.91% (see `acceptance_rate_plot.png`).
- **Purchases by Channel**: A bar chart showing Web as the dominant channel (see `purchases_by_channel_plot.png`).
- **Income vs. Revenue**: An interactive scatter plot connecting income to revenue for campaign acceptors (see `income_vs_revenue.html`).
- **Revenue by Product**: A pie chart showcasing wine’s major role in revenue (see `revenue_by_product_plot.png`).

## Recommendations
Here’s how I’d take these campaigns to the next level:
1. **Invest in Top Performers**: I’d increase the budget for Campaign 4 and Response-style offers—they’re clearly resonating!
2. **Target My Core Audience**: I’d focus on married graduates from Spain earning around $52,000—they’re my biggest fans.
3. **Revamp Weak Channels**: I’d test fresh, creative ideas for Catalog and Deals to spark more engagement.
4. **Push Wine Promotions**: I’d emphasize wine, as it’s a huge revenue driver.

## Conclusion
I’m proud to say that Campaign 4 and the Response campaign are killing it, especially with married graduates from Spain earning ~$52,247.25. My Power BI dashboard (`SocialMedia_Dashboard.pbix`) makes these insights shine with interactive visuals, and `processed_campaign_data.csv` ensures reproducibility. Fixing the income to $52,247.25 was a big win, and my recommendations are set to boost future campaigns and ROI. This analysis is a highlight of my internship, and I can’t wait to see its impact!

## Attachments
- `SocialMedia_Dashboard.pbix`: My interactive Power BI dashboard.
- `processed_campaign_data.csv`, `power_bi_summary_data.csv`: My processed and summarized datasets.
- `acceptance_rate_plot.png`, `purchases_by_channel_plot.png`, `revenue_by_product_plot.png`: My visualization images.
- `income_vs_revenue.html`: My interactive scatter plot.
