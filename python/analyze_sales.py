"""
Retail Sales Analysis
Portfolio project using a synthetic dataset.
Run from the project root: python python/analyze_sales.py
Install dependencies: pip install pandas matplotlib
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "retail_sales_synthetic.csv"
OUTPUT_DIR = ROOT / "python" / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH, parse_dates=["OrderDate"])

print("Shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate OrderIDs:", df["OrderID"].duplicated().sum())

# Basic validation
df = df.drop_duplicates(subset=["OrderID"])
df["Region"] = df["Region"].astype("string").str.strip().str.title()
df["Product"] = df["Product"].astype("string").str.strip()
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
df = df.dropna(subset=["OrderDate", "Sales", "Profit"])

# Exploratory analysis
kpis = {
    "total_sales": round(df["Sales"].sum(), 2),
    "total_profit": round(df["Profit"].sum(), 2),
    "order_count": int(df["OrderID"].nunique()),
    "units_sold": int(df["Quantity"].sum()),
    "average_sales_per_order": round(df["Sales"].mean(), 2),
}
print("\nKPIs:\n", kpis)

region_summary = (
    df.groupby("Region", as_index=False)
      .agg(total_sales=("Sales", "sum"), total_profit=("Profit", "sum"))
      .sort_values("total_sales", ascending=False)
)
product_summary = (
    df.groupby("Product", as_index=False)
      .agg(units_sold=("Quantity", "sum"), total_sales=("Sales", "sum"),
           total_profit=("Profit", "sum"))
      .sort_values("total_profit", ascending=False)
)
monthly_summary = (
    df.assign(Month=df["OrderDate"].dt.to_period("M").astype(str))
      .groupby("Month", as_index=False)
      .agg(total_sales=("Sales", "sum"), total_profit=("Profit", "sum"))
)

region_summary.to_csv(OUTPUT_DIR / "sales_by_region.csv", index=False)
product_summary.to_csv(OUTPUT_DIR / "sales_by_product.csv", index=False)
monthly_summary.to_csv(OUTPUT_DIR / "monthly_sales.csv", index=False)

ax = region_summary.plot(kind="bar", x="Region", y="total_sales", legend=False,
                         title="Sales by Region", rot=30)
ax.set_ylabel("Sales")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sales_by_region.png", dpi=160)
plt.close()

ax = monthly_summary.plot(kind="line", x="Month", y="total_sales", marker="o",
                          title="Monthly Sales Trend", legend=False)
ax.set_ylabel("Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_sales_trend.png", dpi=160)
plt.close()

print("\nTop regions:\n", region_summary.head(3).to_string(index=False))
print("\nTop products by profit:\n", product_summary.head(5).to_string(index=False))
print(f"\nOutputs saved to: {OUTPUT_DIR}")
