import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("archive/Sample - Superstore.csv", encoding='latin1')

# First 5 rows
print(df.head())

# Dataset info
print(df.info())

# Missing values
print(df.isnull().sum())

# ---------------- ANALYSIS ---------------- #

# Top products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

print("\nTop Products:\n")
print(top_products)

# Sales by region
region_sales = df.groupby('Region')['Sales'].sum()

print("\nSales by Region:\n")
print(region_sales)

# Monthly trend
df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Month'] = df['Order Date'].dt.month

monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot()

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()