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

**Source**: [Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

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
├── data/
│   ├── sales_per_category.csv  # Category-wise sales distribution analysis
│   ├── sales_per_product.csv   # Product-level revenue and performance metrics
│   └── sales_trend.csv         # Monthly sales progression and trend data
├── Screenshots/                # Visual documentation of dashboard features
│   ├── The Clusterd Chart.png
│   ├── The DashBoard.png
│   ├── The Donut Chart.png
│   ├── The Highest Revenue Generator.png
│   ├── The Line Chart.png
│   └── The Lowest Revenue Generator.png
├── Ecommerce_Dashboard.pbix    # Power BI dashboard with interactive visualizations
├── README.md                   # Project documentation and setup instructions
├── Task1_Report.docx           # Comprehensive analysis report and recommendations
└── task1_preprocess.py         # Python script for data cleaning and transformation
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
   git clone https://github.com/rwotolara-innocent/Data-Science-&-Analytics-Internship.git
   cd Data-Science-&-Analytics-Internship/FUTURE_DS_01
   ```

2. **Download the dataset**
   - Visit Brazilian E-Commerce Public Dataset on Kaggle
   - Download and extract olist_orders_dataset.csv, olist_order_items_dataset.csv, and olist_products_dataset.csv

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
