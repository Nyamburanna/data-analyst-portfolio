# Retail Sales Analysis Portfolio Project

A beginner-friendly, end-to-end data analytics project using **Excel, SQL, Python, and Power BI**.

> **Data note:** The dataset is synthetic and was generated for practice. It does not represent a real company or actual customer transactions.

## Business questions
1. What are total sales, profit, orders, and units sold?
2. Which regions generate the most sales?
3. Which products contribute the most profit?
4. How do sales change month to month?
5. Which sales channels contribute the largest share of revenue?

## Repository structure
- `data/retail_sales_synthetic.csv` — shared dataset
- `excel/retail_sales_analysis_starter.xlsx` — data sheet and starter summary
- `sql/retail_sales_analysis.sql` — data quality checks and analytical queries
- `python/analyze_sales.py` — cleaning, analysis, exports, and charts
- `powerbi/measures.dax` — starter DAX measures
- `docs/` — add screenshots, final insights, and project notes here

## Tools
- Excel: formulas, summary metrics, PivotTables, charts
- SQL: aggregation, grouping, data quality checks, CTEs, window functions
- Python: pandas, exploratory data analysis, Matplotlib
- Power BI: data model, DAX measures, KPI cards, slicers, and report visuals

## How to use
1. Open the Excel workbook in `excel/`.
2. Import the CSV into a SQL database/table named `sales` and run the queries in `sql/retail_sales_analysis.sql`.
3. Install Python dependencies with `pip install pandas matplotlib`.
4. From the repository root, run `python python/analyze_sales.py`.
5. In Power BI Desktop, import the CSV, create a Date table, add measures from `powerbi/measures.dax`, and build a report.

## Suggested Power BI page
- KPI cards: Total Sales, Total Profit, Total Orders, Profit Margin %
- Bar chart: Sales by Region
- Bar chart: Profit by Product
- Line chart: Monthly Sales
- Slicers: Region, Category, Channel, Date

## Data quality checks to document
- Duplicate order IDs
- Missing values
- Valid date and numeric types
- Sales and profit calculation consistency

## Final deliverable
Replace this section after completing the analysis with 3–5 evidence-based findings, business recommendations, and screenshots of your dashboard. Do not claim results until you have verified them from your analysis.
