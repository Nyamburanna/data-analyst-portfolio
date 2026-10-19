# Step-by-step build guide

## Phase 1 — Excel
1. Open `excel/retail_sales_analysis_starter.xlsx`.
2. Review the `Sales Data` sheet and check data types and filters.
3. Add PivotTables for sales by Region, Category, Product, and month.
4. Add slicers if available, format charts, and make a clear dashboard.
5. Write down three findings based on the actual workbook totals.

## Phase 2 — SQL
1. Import `data/retail_sales_synthetic.csv` into SQLite, PostgreSQL, MySQL, or another SQL environment.
2. Name the table `sales` or adjust the script.
3. Run each query and explain what it answers.
4. Add at least two of your own queries.

## Phase 3 — Python
1. Install Python, or use Google Colab by uploading the CSV and script.
2. Install pandas and matplotlib if needed.
3. Run `python/analyze_sales.py`.
4. Inspect output tables and charts; write a short insight summary.

## Phase 4 — Power BI
1. Install Power BI Desktop from Microsoft's official download page.
2. Import the CSV and confirm column types.
3. Create a Date table and relationship to the order date.
4. Add DAX measures from `powerbi/measures.dax`.
5. Create a report page with KPI cards, charts, and slicers.
6. Save the `.pbix` file locally. GitHub is best for code, documentation, and screenshots; avoid committing very large files.

## Phase 5 — Portfolio polish
1. Replace the placeholder README findings with verified insights.
2. Add screenshots to `docs/`.
3. Add a short section explaining limitations and what you would investigate next.
4. Commit changes with meaningful messages such as `Add monthly sales analysis`.
