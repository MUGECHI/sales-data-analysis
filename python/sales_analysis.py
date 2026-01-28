
import pandas as pd
import matplotlib.pyplot as plt


# Load dataset
file_path = "data/cleaned_dataset.csv"
df = pd.read_csv(file_path)

# Basic checks
print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET INFO")
print(df.info())

# Convert date column
df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%Y')

# ==========================
# 1. MONTHLY SALES TREND
# ==========================
monthly_sales = (
    df.groupby(df['order_date'].dt.to_period('M'))['total_amount']
    .sum()
    .reset_index()
)
monthly_sales.to_csv(
    "outputs/monthly_sales.csv",
    index=False
)
monthly_sales['order_date'] = monthly_sales['order_date'].astype(str)

print("\nMONTHLY SALES")
print(monthly_sales)

plt.figure()
plt.plot(monthly_sales['order_date'], monthly_sales['total_amount'])
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("outputs/monthly_sales_trend.png")
plt.show()

import seaborn as sns
# ==========================
# 2. GENDER SALES
# ==========================
gender_sales = (
    df.groupby('gender')['total_amount']
    .sum()
    .reset_index()
)
gender_sales.to_csv(
    "outputs/gender_sales.csv",
    index=False
)
print("\nGENDER SALES")
print(gender_sales)

plt.figure()
plt.bar(gender_sales['gender'], gender_sales['total_amount'])
plt.title("Total Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("outputs/gender_sales_trend.png")
plt.show()

# ==========================
# 3. CATEGORY SALES
# ==========================
category_sales = (
    df.groupby('product_category')['total_amount']
    .sum()
    .reset_index()
)
category_sales.to_csv(
    "outputs/category_sales.csv",
    index=False
)
print("\nCATEGORY SALES")
print(category_sales)

plt.figure()
plt.bar(category_sales['product_category'], category_sales['total_amount'])
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("outputs/category_sales.png")
plt.show()
# ==========================
# 4. AGE GROUP SALES
# ==========================
bins = [0, 18, 25, 35, 45, 60, 100]
labels = ['<18', '18-25', '26-35', '36-45', '46-60', '60+']

df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

age_sales = (
    df.groupby('age_group')['total_amount']
    .sum()
    .reset_index()
)
age_sales.to_csv(
    "outputs/age_sales.csv",
    index=False
)
print("\nAGE GROUP SALES")
print(age_sales)

plt.figure()
plt.bar(age_sales['age_group'], age_sales['total_amount'])
plt.title("Sales by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("outputs/age_group_sales.png")
plt.show()

# Load dataset
file_path = "/data/cleaned_dataset.csv"
df = pd.read_csv(file_path)

# Preview data
print(df.head())
print(df.info())

