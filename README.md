# Project Title:
- International Debt Analysis

# Project Description:
- The project aim is to analyse the global debt from the given raw data with help of required data analysing tools and to predict the debt analysis for the
future use.

# Objectives:
- Objective of this project is to collect the required raw data, clean the raw data into proper dataset and store in data base for further processing, perform
Exploratory Data Analysis (EDA) to identify debt trends, country insights and financial indicators and show the performed data in interactive dashboard using data
visualization tools.

# Technologies Used:
- Python is used for programming, where data cleaning is done. It acts as interface between MySQL and Stream lit with help of coding.
- Pandas is a python library, used to read the raw data file and convert it into data frame for processing.
- MySQL acts as database, where cleaned data’s can be inserted for further use.
- Plotly is for data visualization, where cleaned data can be transformed into useful chart for prediction.
- Stream lit acts as a user interface and interactive dashboard, where the data’s can be visualized.

# Dataset:
- Source : International Debt Statistics Jan 2022 - Dataset

# Table Structure:
<img width="1578" height="669" alt="image" src="https://github.com/user-attachments/assets/647d0267-76db-4a2c-ba71-1b84318ba64c" />






























# SQL Analysis:
# SQL Analytical Questions (30)

# Basic Queries
# 1. Retrieve all distinct country names from the dataset.
select country_name from country_table;

# 2. Count the total number of countries available.
select count(country_name) as total_no_of_countries from country_table;

# 3. Find the total number of indicators present.
select count(series_name) as total_no_of_indicators from series_table;  

# 4. Display the first 10 records of the dataset.
select * from debt_fact_table limit 10;
select c.country_name, s.series_name, d.year, d.value from debt_fact_table d 
join country_table c on c.country_code = d.country_code join series_table s on s.series_code = d.series_code limit 10 ;

# 5. Calculate the total global debt.
select sum(value) as total_global_debt from debt_fact_table;

# 6. List all unique indicator names.
select series_name as unique_indicator_name from series_table;

# 7. Find the number of records for each country.
select c.country_name, count(*) as no_of_records from debt_fact_table d join country_table c 
on c.country_code = d.country_code group by c.country_name;

select c.country_name, count(*) as no_of_records from debt_fact_table d join country_table c 
 on c.country_code = d.country_code group by c.country_name order by no_of_records Desc;

# 8. Display all records where debt is greater than 1 billion USD.
select * from debt_fact_table where value > '1000000000' order by value Asc;

# 9. Find the minimum, maximum, and average debt values.
select min(value) as min_debt_value, max(value) as max_debt_value, avg(value) as avg_debt_value 
from debt_fact_table where value > '0';

# 10. Count total number of records in the dataset.
select count(*) as total_no_records from debt_fact_table;



# Intermediate Level
# 1. Find the total debt for each country.
select c.country_name, sum(d.value) as total_debt from debt_fact_table d join country_table c 
on c.country_code = d.country_code group by c.country_name;

# 2. Display the top 10 countries with the highest total debt.
select c.country_name, sum(d.value) as highest_total_debt, sum(d.value) as lowest_total_debt 
from debt_fact_table d join country_table c on c.country_code = d.country_code 
group by c.country_Name order by highest_total_debt desc limit 10;

select c.country_name, sum(d.value) as lowest_total_debt from debt_fact_table d join country_table c 
on c.country_code = d.country_codegroup by c.country_name order by lowest_total_debt asc limit 10;

# 3. Find the average debt per country.
select c.country_name, avg(d.value) as average_debt from debt_fact_table d join country_table c 
on c.country_code = d.country_code group by c.country_name order by average_debt desc;

# 4. Calculate total debt for each indicator.
select s.series_name, sum(d.value) as total_debt from debt_fact_table d join series_table s 
on s.series_code = d.series_code group by s.series_name;

# 5. Identify the indicator contributing the highest total debt.
select s.series_name, sum(d.value) as highest_total_debt from debt_fact_table d join series_table s on s.series_code = d.series_code 
group by s.series_name order by highest_total_debt desc limit 10;

select s.series_name, sum(d.value) as lowest_total_debt from debt_fact_table d join series_table s on s.series_code = d.series_code 
group by s.series_name having lowest_total_debt > 0 order by lowest_total_debt asc limit 10 ;

# 6. Find the country with the lowest total debt.
select c.country_name, sum(d.value) as lowest_total_debt from debt_fact_table d join country_table c on c.country_code = d.country_code
group by c.country_name order by lowest_total_debt asc limit 1;

# 7. Calculate total debt for each country and indicator combination.
select c.country_name, s.series_name, sum(d.value) as total_debt from debt_fact_table d join country_table c on c.country_code = d.country_code
join series_table s on s.series_code = d.series_code group by c.country_name, s.series_name;

# 8. Count how many indicators each country has.
select c.country_name, Count(s.series_code) as total_indicators from country_series_table cs join country_table c on c.country_code = cs.country_code
join series_table s on s.series_code = cs.series_code group by cs.country_code;

select c.country_name, Count(s.series_code) as total_indicators from debt_fact_table d join country_table c on c.country_code = d.country_code
join series_table s on s.series_code = d.series_code group by d.country_code;

# 9. Display countries whose total debt is above the global average.
with global_avg As
 ( Select avg(Value) as avg_value from debt_fact_table )
select c.country_Name, sum(d.value) as total_debt from debt_fact_table d join country_table c on c.country_code = d.country_code 
group by c.country_name Having total_debt > (select avg_value from global_avg);

# 10. Rank countries based on total debt (highest to lowest).
select dense_rank() over ( order by Sum(d.value) desc) as debt_rank, c.country_Name, Sum(d.value) as total_debt 
from debt_fact_table d join country_table c on c.country_code = d.country_code group by c.country_name order by total_debt Desc;



# Advanced level
# 1. Find the top 5 indicators contributing most to global debt.
select s.Series_Name, sum(d.Value) as total_debt from debt_fact_table d join series_table s on s.Series_Code = d.Series_Code 
group by s.Series_Name order by total_debt Desc limit 5;

# 2. Calculate percentage contribution of each country to total global debt.
with global_total_debt as (
select sum(value) as total_global_debt from debt_fact_table)
select c.country_name, sum(d.value) as total_debt, cast((((sum(d.value)) / (select total_global_debt from global_total_debt)) * 100) as decimal (20,2)) as percentage_value 
from debt_fact_table d join country_table c on c.country_code = d.country_code group by c.country_name;

# 3. Identify the top 3 countries for each indicator based on debt.
SELECT country_name, series_name, total_debt
FROM (
    SELECT c.country_name, s.series_name, SUM(d.value) AS total_debt,
        ROW_NUMBER() OVER ( PARTITION BY s.series_name ORDER BY SUM(d.value) DESC ) AS rank_num FROM debt_fact_table d 
        JOIN country_table c ON c.country_code = d.country_code JOIN series_table s ON s.series_code = d.series_code 
        GROUP BY c.country_name, s.series_name
) ranked
WHERE rank_num <= 3;

# 4. Find the difference between maximum and minimum debt for each country.
select c.country_name, max(d.value) as max_debt, min(d.value) as min_debt, (max(d.value) - min(d.value) ) as dif_max_min 
from debt_fact_table d join country_table c on c.country_code = d.country_code group by c.country_name;

select c.country_name, max(d.value) as max_debt, min(d.value) as min_debt, (max(d.value) - min(d.Value) ) as dif_max_min 
from debt_fact_table d join country_table c on c.country_code = d.country_code where d.Value > '0' group by c.country_name;

# 5. Create a view for the top 10 countries with highest debt.
CREATE VIEW top_10_countries_highest_debt AS
SELECT c.country_name, SUM(d.value) AS highest_debt FROM debt_fact_table d JOIN country_table c ON c.country_code = d.country_code
GROUP BY c.country_name ORDER BY highest_debt DESC LIMIT 10;
select * from top_10_countries_highest_debt;

# 6. Categorize countries into: High Debt Medium Debt Low Debt (based on thresholds)
SELECT c.country_name, SUM(d.value) AS total_debt,
    CASE 
        WHEN SUM(d.value) > 5000000000000 THEN 'High Debt'
        WHEN SUM(d.value) BETWEEN 1000000000000 AND 5000000000000 THEN 'Medium Debt'
        ELSE 'Low Debt'
    END AS debt_category
FROM debt_fact_table d JOIN country_table c ON c.country_code = d.country_code GROUP BY c.country_name ORDER BY total_debt DESC;

# 7. Use window functions to calculate cumulative debt per country.
WITH debt_data AS (
    SELECT c.country_name, d.year,  d.value FROM debt_fact_table d JOIN country_table c  ON c.country_code = d.country_code
)
SELECT country_name, year, value, SUM(value) OVER (
        PARTITION BY country_name 
        ORDER BY year
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_debt
FROM debt_data ORDER BY country_name, year;

# 8. Find indicators where average debt is higher than overall average debt.
with global_avg as ( select cast(avg(value) as decimal(20,2)) as avg_value from debt_fact_table )
select s.series_name, cast(avg(d.value) as decimal(20,2)) as average_debt from debt_fact_table d join series_table s
 on s.series_code = d.series_code group by s.series_name having average_debt > (select avg_value from global_avg);

# 9. Identify countries contributing more than 5% of global debt. -> with - comm table exppresion (temp table)
with global_tot_debt as (select sum(value) as total_global_debt from debt_fact_table)
select c.country_name, sum(d.value) as total_debt, cast((((sum(d.value)) / (select total_global_debt from global_tot_debt)) * 100) 
as decimal(20,2)) as percentage_value 
from debt_fact_table d join country_table c on c.country_code = d.country_code 
group by c.country_name having percentage_value > 5 order by total_debt Desc;

# 10. Find the most dominant indicator (highest contribution) for each country.
WITH country_indicator_totals AS (
    SELECT c.country_name, s.series_name, SUM(d.value) AS total_value  FROM debt_fact_table d JOIN country_table c 
        ON c.country_code = d.country_code JOIN series_table s ON s.series_code = d.series_code 
        GROUP BY c.country_name, s.series_name ),
ranked_indicators AS ( SELECT *,  ROW_NUMBER() OVER ( PARTITION BY country_name ORDER BY total_value DESC ) AS rn 
FROM country_indicator_totals )
SELECT country_name, series_name, total_value AS highest_contribution FROM ranked_indicators WHERE rn = 1
ORDER BY highest_contribution DESC;


