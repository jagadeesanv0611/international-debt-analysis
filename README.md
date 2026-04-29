# Project Title:
International Debt Analysis

# Project Description:
This project analyzes international debt data using Python, SQL, and data visualization techniques to identify debt trends, country-level insights, and financial indicators through exploratory data analysis and interactive dashboards.

# Objectives:
The objective of this project is to design and implement an International Debt Analytics System
- Data Collection:
       Load the raw CSV into a Pandas DataFrame to analyze its structure, column distributions, and underlying data types.
- Data Cleaning & Preprocessing
       Clean the dataset by handling nulls and duplicates, converting data types, and filtering for essential columns to ensure a standardized,
       high-quality input for analysis.
- Exploratory Data Analysis (EDA):
        To evaluate country-wise debt distribution, identify highest and lowest debt countries, analyze debt indicators, uncover patterns and trends, and
        generate statistical insights.
- Data Storage (SQL):
        Design and implement a relational database in MySQL by creating tables for countries, indicators, and debt data, inserting cleaned data,
        defining primary and foreign keys, and writing SQL queries for analysis.
- Data Visualization:
        Develop data visualizations by connecting the SQL database to Streamlit app and creating dashboards with Matplotlib to
        present country-wise and indicator-wise debt insights.

# Technologies Used:
- Python is used for Data processing.
- Pandas and Numpy is used for Data Manipulation.
- MYSQL is used for Data Storage.
- Matplotlib for Data visualization.
- Streamlit is used as User Interface which acts as dashboards.

# Dataset Information:
- Dataset Source: International Debt Statistics Jan 2022 - Dataset
- It includes, Country Name, Debt indicators, Year-wise financial values.

# Project Workflow:
- Data processing done by handling missing and duplicate values.
- Load the correct CSV file into pandas Dataframe.
- Performing Exploratory Data Analysis (EDA) to analyse patterns, trends and distributions
- Create structured relational database by Normalization
- Ensure accurate data is inserted from Python to SQL
- Write optimized SQL queries using joins and aggregations
- Data visualiztion tools to build charts and build structured dashboards.
  
# Insights and Reporting:
- Country-wise debt distribution
- Top countries with highest and lowest debt
- Debt distribution across different indicators
- Trends and patterns in international debt.

# SQL Analysis:
# SQL Analytical Questions (30) :
# Basic Queries:
1. Retrieve all distinct country names from the dataset.
- select Country_Name from country_table;

2. Count the total number of countries available.
- select count(Country_Name) as total_no_of_countries from country_table;

3. Find the total number of indicators present.
- select count(Series_Name) as total_no_of_indicators from series_table;

4. Display the first 10 records of the dataset.
- select c.Country_Name, s.Series_Name, d.Year, d.Value from debt_fact_table d
join country_table c on c.Country_Code = d.Country_Code join series_table s on s.Series_Code = d.Series_Code limit 10 ;

5. Calculate the total global debt.
- select sum(Value) as total_global_debt from debt_fact_table;

6. List all unique indicator names.
- select Series_Name as Unique_indicator_name from series_table;

7. Find the number of records for each country.
- select c.Country_Name, count(*) as no_of_records from debt_fact_table d join country_table c 
 on c.Country_Code = d.Country_Code group by c.Country_Name order by no_of_records Desc;

8. Display all records where debt is greater than 1 billion USD.
- select * from debt_fact_table where value > '1000000000' order by Value Asc;

9. Find the minimum, maximum, and average debt values.
- select min(Value) as min_debt_value, max(Value) as max_debt_value, avg(Value) as avg_debt_value from debt_fact_table;

10. Count total number of records in the dataset.
- select count(*) as total_no_records from debt_fact_table;

# Intermediate Level:
1. Find the total debt for each country.
- select c.Country_Name, sum(d.Value) as total_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name;

2. Display the top 10 countries with the highest total debt.
- select c.Country_Name, sum(d.Value) as highest_total_debt, sum(d.Value) as lowest_total_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name order by highest_total_debt desc limit 10;

- select c.Country_Name, sum(d.Value) as lowest_total_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code
group by c.Country_Name order by lowest_total_debt asc limit 10;

3. Find the average debt per country.
- select c.Country_Name, avg(d.value) as average_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code 
group by c.Country_Name order by average_debt desc;

4. Calculate total debt for each indicator.
- select s.Series_Name, sum(d.Value) as total_debt from debt_fact_table d join series_table s on s.Series_Code = d.Series_Code group by s.Series_Name;

5. Identify the indicator contributing the highest total debt.
- select s.Series_Name, sum(d.Value) as highest_total_debt from debt_fact_table d join series_table s on s.Series_Code = d.Series_Code 
group by s.Series_Name order by highest_total_debt desc limit 10;

- select s.Series_Name, sum(d.Value) as lowest_total_debt from debt_fact_table d join series_table s on s.Series_Code = d.Series_Code 
group by s.Series_Name having lowest_total_debt > 0 order by lowest_total_debt asc limit 10 ;

6. Find the country with the lowest total debt.
- select c.Country_Name, sum(d.Value) as lowest_total_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code
group by c.Country_Name order by lowest_total_debt asc limit 1;

7. Calculate total debt for each country and indicator combination.
- select c.Country_Name, s.Series_Name, sum(d.value) as total_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code
join series_table s on s.Series_Code = d.Series_Code group by c.Country_Name, s.Series_Name;

8. Count how many indicators each country has.
- select c.Country_Name, Count(s.Series_Code) as total_indicators from country_series_table cs join country_table c on c.Country_Code = cs.Country_Code
join series_table s on s.Series_Code = cs.Series_Code group by cs.Country_Code;

9. Display countries whose total debt is above the global average.
- with global_avg As  ( Select avg(Value) as avg_value from debt_fact_table )
select c.Country_Name, sum(d.value) as total_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code 
group by c.Country_Name Having total_debt > (select avg_value from global_avg);

10. Rank countries based on total debt (highest to lowest).
- select dense_rank() over ( order by Sum(d.Value) desc) as debt_rank, c.Country_Name, Sum(d.Value) as total_debt from debt_fact_table d 
join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name order by total_debt Desc;


# Advanced level:
1. Find the top 5 indicators contributing most to global debt.
select s.Series_Name, sum(d.Value) as total_debt from debt_fact_table d join series_table s on s.Series_Code = d.Series_Code 
group by s.Series_Name order by total_debt Desc limit 5;

2. Calculate percentage contribution of each country to total global debt.
with global_total_debt as (select sum(Value) as total_global_debt from debt_fact_table)
select c.Country_Name, sum(d.Value) as total_debt, cast((((sum(d.Value)) / (select total_global_debt from global_total_debt)) * 100) as decimal (20,2)) as
Percentage_value from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name;

3. Identify the top 3 countries for each indicator based on debt.
SELECT Country_Name, Series_Name, total_debt
FROM (
    SELECT c.Country_Name, s.Series_Name, SUM(d.Value) AS total_debt,
        ROW_NUMBER() OVER ( PARTITION BY s.Series_Name ORDER BY SUM(d.Value) DESC ) AS rank_num FROM debt_fact_table d 
        JOIN country_table c ON c.Country_Code = d.Country_Code JOIN series_table s ON s.Series_Code = d.Series_Code GROUP BY c.Country_Name, s.Series_Name
) ranked
WHERE rank_num <= 3;

4. Find the difference between maximum and minimum debt for each country.
select c.Country_Name, max(d.value) as max_debt, min(d.Value) as min_debt, (max(d.value) - min(d.Value) ) as dif_max_min from debt_fact_table d 
join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name;

select c.Country_Name, max(d.value) as max_debt, min(d.Value) as min_debt, (max(d.value) - min(d.Value) ) as dif_max_min from debt_fact_table d 
join country_table c on c.Country_Code = d.Country_Code where d.Value > '0' group by c.Country_Name;

5. Create a view for the top 10 countries with highest debt.
CREATE VIEW top_10_countries_highest_debt AS
SELECT c.Country_Name, SUM(d.Value) AS highest_debt FROM debt_fact_table d JOIN country_table c ON c.Country_Code = d.Country_Code
GROUP BY c.Country_Name ORDER BY highest_debt DESC LIMIT 10;

select * from top_10_countries_highest_debt;

6. Categorize countries into:
    High Debt
    Medium Debt
    Low Debt (based on thresholds)
SELECT c.Country_Name, SUM(d.Value) AS total_debt,
    CASE 
        WHEN SUM(d.Value) > 5000000000000 THEN 'High Debt'
        WHEN SUM(d.Value) BETWEEN 1000000000000 AND 5000000000000 THEN 'Medium Debt'
        ELSE 'Low Debt'
    END AS debt_category
FROM debt_fact_table d JOIN country_table c ON c.Country_Code = d.Country_Code GROUP BY c.Country_Name ORDER BY total_debt DESC;

7. Use window functions to calculate cumulative debt per country.
select c.Country_Name, d.Year, d.Value, LAG(d.Value) over (partition by c.Country_Name order by d.Year) as previous_debt, 
((LAG(d.Value) over (partition by c.Country_Name order by d.Year)) + (d.Value)) as cumulati_value
from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code;

select c.Country_Name, d.Year, d.Value, sum(d.Value) over (partition by c.Country_Name order by d.Year) as cumulative_debt, 
(lag((sum(d.Value) over (partition by c.Country_Name order by d.Year)) + (d.Value))) as original_cumu_value
from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code;

8. Find indicators where average debt is higher than overall average debt.
with global_avg as ( select cast(avg(Value) as decimal(20,2)) as avg_value from debt_fact_table )
select s.Series_Name, cast(avg(d.Value) as decimal(20,2)) as average_debt from debt_fact_table d join series_table s on s.Series_Code = d.Series_Code
group by s.Series_Name having average_debt > (select avg_value from global_avg);

9. Identify countries contributing more than 5% of global debt.  ->  with - comm table exppresion (temp table)
with global_tot_debt as (select sum(value) as total_global_debt from debt_fact_table)
select c.Country_Name, sum(d.Value) as total_debt, cast((((sum(d.Value)) / (select total_global_debt from global_tot_debt)) * 100) as decimal(20,2)) as percentage_value 
from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name having percentage_value > 5 order by total_debt Desc;

10. Find the most dominant indicator (highest contribution) for each country.  







