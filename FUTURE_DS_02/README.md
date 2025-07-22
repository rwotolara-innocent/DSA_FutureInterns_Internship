# Task 2: Social Media Campaign Performance Tracker

## Overview

This project develops an interactive Power BI dashboard for analyzing social media ad campaign performance. Using the Facebook Ad Campaign Dataset, I calculated key metrics like click-through rate (CTR) and return on investment (ROI) to provide actionable insights for optimizing marketing strategies.

## Business Problem
Social media marketing requires data-driven insights to maximize ad spend efficiency and engagement. This dashboard addresses key questions:
- Which campaigns deliver the highest CTR and ROI?
- How do impressions, clicks, and conversions correlate with costs?
- Which platforms or campaigns perform best?

## Dataset
**Source**: [Facebook Ad Campaign Dataset](https://www.kaggle.com/datasets/madislemsalu/facebook-ad-campaign)

**Description**: A clean dataset with ad campaign metrics, including impressions, clicks, conversions, and costs.
- **Key Columns**: Campaign name, platform, impressions, clicks, conversions, cost, revenue
- **Why Chosen**: The dataset is straightforward, free, and contains all necessary metrics for performance analysis.

## Technical Implementation

### Data Processing Pipeline
```python
# Key transformations performed:
- Load and clean ad campaign data
- Auto-detect column names for flexibility
- Calculate CTR and ROI
- Aggregate data by campaign for performance analysis
- Export results to CSV for Power BI
```

### Key Metrics Calculated
- **Click-Through Rate (CTR)**: (Clicks / Impressions) * 100
- **Return on Investment (ROI)**: ((Conversions * Average Value - Cost) / Cost) * 100
- **Campaign Performance**: Total impressions, clicks, conversions, and spend per campaign
- **Platform Insights**: Aggregated metrics by platform

## Project Structure

```
├── Data/
│   ├── facebook_powerbi_data.csv     # Processed campaign-level metrics
├── Screenshots/
│   ├── Campaign_CTR_Bar.png         # Bar chart of campaign CTR
│   ├── Platform_Comparison.png      # Platform performance comparison
│   └──  ROI_Summary.png              # Summary of ROI by campaign
├── facebook_ad_analysis.py           # Python script for data processing and metric calculation
├── README.md                         # Project documentation and setup instructions
├── SocialMedia_Dashboard.pbix        # Power BI dashboard with interactive visualizations
└── Task2_Summary.docx               # Report with key findings and recommendations
```

## Key Insights Discovered

### Campaign Performance
- **High-ROI Campaigns**: Identified campaigns with strong ROI for budget allocation
- **Engagement Metrics**: Highlighted campaigns with high CTR for optimization
- **Platform Analysis**: Compared platform performance to guide marketing strategies

### Business Recommendations
1. **Budget Allocation**: Increase spend on high-ROI campaigns
2. **Campaign Optimization**: Focus on campaigns with high CTR for better engagement
3. **Platform Strategy**: Prioritize platforms with strong performance metrics

## Setup Instructions

### Prerequisites
```bash
# Required software
- Python 3.8+
- Power BI Desktop (free)
- Git

# Python dependencies
pip install pandas
```

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/Data-Science-Analytics-Internship.git
   cd Data-Science-Analytics-Internship/FUTURE_DS_02
    ```

2. **Download the dataset**
   - Visit Facebook Ad Campaign Dataset on Kaggle 
   - Download and extract `facebook_ad_campaign.csv`

3. **Run data preprocessing**
 ```bash
python facebook_ad_analysis.py
 ```

4. **Open Power BI dashboard**
   - Launch Power BI Desktop
   - Open `SocialMedia_Dashboard.pbix`
   - Refresh data connections if needed

## Dashboard Features

### Interactive Visualizations
- **Campaign Performance**: Bar charts and tables showing CTR and ROI
- **Platform Comparison**: Visuals comparing metrics across platforms
- **KPI Cards**: Key metrics like total impressions, clicks, and spend
- **Trend Analysis**: Charts showing campaign performance over time

### Filtering Capabilities
- Campaign selection
- Platform filtering
- Date range adjustments
- Metric-based sorting

## Technical Skills Demonstrated

**Data Processing**: Data cleaning, metric calculation, and aggregation
**Analytics**: Performance analysis and ROI modeling
**Visualization**: Interactive dashboard design with Power BI
**Python**: pandas for data manipulation and processing
**Business Intelligence**: KPI development and actionable insights

## Results Impact

This dashboard enables stakeholders to:
- Optimize ad spend based on ROI and CTR
-Identify high-performing campaigns and platforms
- Monitor marketing performance in real-time
- Make data-driven marketing decisions

## Future Enhancements

- **Predictive Modeling**: Forecast campaign performance
- **A/B Testing Analysis**: Compare ad variations
- **Real-time Data**: Integrate live campaign data
- **Advanced Metrics**: Include cost-per-click and cost-per-conversion

## Contact

For questions about this projectincome: project or collaboration opportunities, please reach out!

*This project is part of my Data Science & Analytics internship portfolio, showcasing skills in marketing analytics and data visualization.*
