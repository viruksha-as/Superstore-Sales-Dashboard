-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM superstore;

-- Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM superstore;

-- Sales by Region
SELECT Region,
SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;

-- Top 10 Products
SELECT [Product Name],
SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY [Product Name]
ORDER BY Total_Sales DESC
LIMIT 10;

-- Category Wise Sales
SELECT Category,
SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category;

-- Monthly Sales Trend
SELECT MONTH([Order Date]) AS Month,
SUM(Sales) AS TotalSales
FROM superstore
GROUP BY MONTH([Order Date])
ORDER BY Month;