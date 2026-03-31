import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales.csv")

print(df.head())
print(df.info())
print(df.describe())

df["Total_Sales"] = df["Quantity"] * df["Price"]

sales_by_product = df.groupby("Product")["Total_Sales"].sum()
print(sales_by_product)

plt.figure(figsize=(10,6))
sns.barplot(x=sales_by_product.index, y=sales_by_product.values)
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

sales_by_category = df.groupby("Category")["Total_Sales"].sum()
print(sales_by_category)

df["Date"] = pd.to_datetime(df["Date"])   
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Total_Sales"].sum()
print(monthly_sales)
