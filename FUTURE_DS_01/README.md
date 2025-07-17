# Task 1: Business Sales Dashboard

## Overview

This project develops an interactive Power BI dashboard for comprehensive e-commerce business analytics. Using the Brazilian E-Commerce dataset, I analyzed sales performance, identified top-performing products, and uncovered revenue trends to support data-driven business decisions.

## Business Problem

E-commerce businesses need actionable insights to optimize their product portfolio and maximize revenue. This dashboard addresses key questions:
- Which products drive the highest sales volume?
- What are the seasonal trends in revenue?
- Which product categories generate the most profit?
- How can inventory and marketing strategies be optimized?

## Dataset

**Source**: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**Description**: Comprehensive dataset containing 100,000+ real commercial orders from 2016-2018
- **Orders**: 99,441 orders with timestamps and status
- **Products**: 32,951 products across multiple categories
- **Customers**: Geographic distribution across Brazil
- **Sellers**: 3,095 sellers with location data

**Key Files Used**:
- `olist_orders_dataset.csv` - Order information and timestamps
- `olist_order_items_dataset.csv` - Product details and pricing
- `olist_products_dataset.csv` - Product categories and specifications

## Technical Implementation

### Data Processing Pipeline
```python
# Key transformations performed:
- Data cleaning and validation
- Multi-table joins across order, product, and item datasets
- Date parsing and temporal feature engineering
- Revenue calculations and aggregations
- Category-wise performance metrics
```

### Key Metrics Calculated
- **Sales Volume**: Total units sold per product/category
- **Revenue Analysis**: Total and average order values
- **Temporal Trends**: Monthly and quarterly sales patterns
- **Category Performance**: Revenue distribution across product categories
- **Geographic Insights**: Sales distribution by customer location

## Project Structure

```
├── task1_preprocess.py          # Data preprocessing and cleaning
├── Ecommerce_Dashboard.pbix     # Interactive Power BI dashboard
├── Task1_Report.docx           # Executive summary and insights
├── data/
│   ├── sales_per_product.csv   # Processed product-level metrics
│   ├── sales_per_category.csv  # Category performance data
│   └── sales_trend.csv         # Time-series analysis data
└── README.md                   # This file
```

## Key Insights Discovered

### Top Performers
- **Best-selling Category**: Health & Beauty products dominated sales volume
- **Highest Revenue**: Computer accessories generated premium revenue per unit
- **Seasonal Patterns**: Strong holiday season performance in Q4

### Business Recommendations
1. **Inventory Optimization**: Increase stock for high-performing categories
2. **Marketing Focus**: Allocate budget to proven revenue drivers
3. **Seasonal Planning**: Prepare for Q4 demand surge

## Setup Instructions

### Prerequisites
```bash
# Required software
- Python 3.8+
- Power BI Desktop (free)
- Git

# Python dependencies
pip install pandas numpy matplotlib seaborn
```

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Data-Science-&-Analytics-Internship.git
   cd Data-Science-&-Analytics-Internship/Task1
   ```

2. **Download the dataset**
   - Visit [Kaggle dataset page](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
   - Download and extract to `data/raw/` folder

3. **Run data preprocessing**
   ```bash
   python task1_preprocess.py
   ```

4. **Open Power BI dashboard**
   - Launch Power BI Desktop
   - Open `Ecommerce_Dashboard.pbix`
   - Refresh data connections if needed

## Dashboard Features

### Interactive Visualizations
- **Sales Trends**: Time-series charts showing monthly/quarterly performance
- **Product Rankings**: Top 10 products by sales volume and revenue
- **Category Analysis**: Pie charts and bar graphs for category comparison
- **Geographic Distribution**: Map visualization of sales by region
- **KPI Cards**: Key performance indicators at a glance

### Filtering Capabilities
- Date range selection
- Product category filtering
- Geographic region filtering
- Revenue threshold adjustments

## Technical Skills Demonstrated

- **Data Engineering**: ETL pipeline development, data cleaning and validation
- **Analytics**: Statistical analysis, trend identification, performance metrics
- **Visualization**: Interactive dashboard design, storytelling with data
- **Business Intelligence**: KPI development, executive reporting
- **Python**: pandas, data manipulation, automated reporting

## Results Impact

This dashboard enables stakeholders to:
- Make data-driven inventory decisions
- Optimize marketing spend allocation
- Identify growth opportunities
- Monitor business performance in real-time
- Generate automated executive reports

## Future Enhancements

- **Predictive Analytics**: Sales forecasting models
- **Customer Segmentation**: RFM analysis and customer lifetime value
- **Real-time Integration**: Live data streaming capabilities
- **Advanced Metrics**: Cohort analysis and retention rates

## Contact

For questions about this project or collaboration opportunities, please reach out!

---

*This project is part of my Data Science & Analytics internship portfolio, demonstrating practical business intelligence and data visualization skills.*
