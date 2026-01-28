-- Sales Data Analysis Queries
-- Project: Sales Data Analysis
-- Author: Jane Waithira Mugechi
-- Database: sales_analysis

-- 1. Total transactions and revenue
SELECT
  COUNT(*) AS total_transactions,
  SUM(total_amount) AS total_sales
FROM sales;

-- 2. Sales by product category
SELECT
  product_category,
  SUM(total_amount) AS category_sales
FROM sales
GROUP BY product_category
ORDER BY category_sales DESC;

-- 3. Monthly sales trend
SELECT
  DATE_FORMAT(order_date_fixed, '%Y-%m') AS month,
  SUM(total_amount) AS monthly_sales
FROM sales
GROUP BY month
ORDER BY month;

-- 4. Average order value
SELECT
  ROUND(AVG(total_amount), 2) AS avg_order_value
FROM sales;

-- 5. Sales by gender
SELECT
  gender,
  SUM(total_amount) AS total_sales
FROM sales
GROUP BY gender
ORDER BY total_sales DESC;

-- 6. Top 5 customers by revenue
SELECT
  customer_id,
  SUM(total_amount) AS customer_sales
FROM sales
GROUP BY customer_id
ORDER BY customer_sales DESC
LIMIT 5;

-- 7. Data quality check
SELECT
  COUNT(*) AS bad_rows
FROM sales
WHERE order_date_fixed IS NULL
   OR total_amount <= 0;

-- ==============================
-- SQL Views for Reporting
-- ==============================

-- Monthly sales trend view
CREATE OR REPLACE VIEW monthly_sales AS
SELECT
  DATE_FORMAT(order_date_fixed, '%Y-%m') AS month,
  SUM(total_amount) AS monthly_sales
FROM sales
GROUP BY month;

-- Sales by product category view
CREATE OR REPLACE VIEW category_sales AS
SELECT
  product_category,
  SUM(total_amount) AS total_sales
FROM sales
GROUP BY product_category;

-- Sales by gender view
CREATE OR REPLACE VIEW gender_sales AS
SELECT
  gender,
  SUM(total_amount) AS total_sales
FROM sales
GROUP BY gender;
