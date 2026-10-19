-- Retail Sales Analysis (SQLite-compatible)
-- Dataset: ../data/retail_sales_synthetic.csv
-- Import the CSV into a table named sales before running these queries.

-- 1. Basic data quality checks
SELECT COUNT(*) AS row_count FROM sales;
SELECT OrderID, COUNT(*) AS occurrences
FROM sales GROUP BY OrderID HAVING COUNT(*) > 1;
SELECT
  SUM(CASE WHEN OrderDate IS NULL OR OrderDate = '' THEN 1 ELSE 0 END) AS missing_dates,
  SUM(CASE WHEN Product IS NULL OR Product = '' THEN 1 ELSE 0 END) AS missing_products
FROM sales;

-- 2. Overall KPIs
SELECT
  ROUND(SUM(Sales), 2) AS total_sales,
  ROUND(SUM(Profit), 2) AS total_profit,
  COUNT(DISTINCT OrderID) AS total_orders,
  SUM(Quantity) AS units_sold
FROM sales;

-- 3. Sales and profit by region
SELECT Region, ROUND(SUM(Sales), 2) AS total_sales,
       ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY Region
ORDER BY total_sales DESC;

-- 4. Product performance
SELECT Product, SUM(Quantity) AS units_sold,
       ROUND(SUM(Sales), 2) AS total_sales,
       ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY Product
ORDER BY total_profit DESC;

-- 5. Monthly trend
SELECT substr(OrderDate, 1, 7) AS order_month,
       ROUND(SUM(Sales), 2) AS monthly_sales,
       ROUND(SUM(Profit), 2) AS monthly_profit
FROM sales
GROUP BY substr(OrderDate, 1, 7)
ORDER BY order_month;

-- 6. Channel performance with a window function
WITH channel_summary AS (
  SELECT Channel, SUM(Sales) AS total_sales
  FROM sales
  GROUP BY Channel
)
SELECT Channel, ROUND(total_sales, 2) AS total_sales,
       ROUND(100.0 * total_sales / SUM(total_sales) OVER (), 2) AS sales_share_pct
FROM channel_summary
ORDER BY total_sales DESC;
