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
<img width="1090" height="332" alt="image" src="https://github.com/user-attachments/assets/560c8035-cdf6-4608-a75b-7630ead2176f" />

# 2. Count the total number of countries available.
select count(country_name) as total_no_of_countries from country_table;
<img width="1090" height="333" alt="image" src="https://github.com/user-attachments/assets/bfd999fe-e39a-45af-841e-a71d034e57a6" />

# 3. Find the total number of indicators present.
select count(series_name) as total_no_of_indicators from series_table;  
<img width="1090" height="322" alt="image" src="https://github.com/user-attachments/assets/95db7bfe-4902-40b9-b3a4-1ee53df411c1" />


# 4. Display the first 10 records of the dataset.
select * from debt_fact_table limit 10;
<img width="1090" height="334" alt="image" src="https://github.com/user-attachments/assets/d2226632-927b-4837-b7c6-0fa4839a54f0" />

select c.country_name, s.series_name, d.year, d.value from debt_fact_table d 
join country_table c on c.country_code = d.country_code join series_table s on s.series_code = d.series_code limit 10 ;
<img width="1090" height="343" alt="image" src="https://github.com/user-attachments/assets/fd80320f-5d4e-4be7-84a4-dc0217814bb2" />

# 5. Calculate the total global debt.
select sum(value) as total_global_debt from debt_fact_table;
<img width="1090" height="298" alt="image" src="https://github.com/user-attachments/assets/bccee507-f2cd-4bde-ae4a-22d5051b79ad" />

# 6. List all unique indicator names.
select series_name as unique_indicator_name from series_table;
<img width="1090" height="301" alt="image" src="https://github.com/user-attachments/assets/03fe9a83-6635-4f8a-8da9-f70ca5bbf3d2" />

# 7. Find the number of records for each country.
select c.country_name, count(*) as no_of_records from debt_fact_table d join country_table c 
on c.country_code = d.country_code group by c.country_name;
<img width="1090" height="314" alt="image" src="https://github.com/user-attachments/assets/4060f21b-4d17-4f4b-96e8-101bff185c9d" />

select c.country_name, count(*) as no_of_records from debt_fact_table d join country_table c 
 on c.country_code = d.country_code group by c.country_name order by no_of_records Desc;
<img width="1090" height="304" alt="image" src="https://github.com/user-attachments/assets/8bcd033b-bbe5-4e79-837a-d8f52a38a691" />

# 8. Display all records where debt is greater than 1 billion USD.
select * from debt_fact_table where value > '1000000000' order by value Asc;
<img width="1090" height="299" alt="image" src="https://github.com/user-attachments/assets/f7119d48-2c8f-4d94-8237-51463b91cef3" />

# 9. Find the minimum, maximum, and average debt values.
select min(value) as min_debt_value, max(value) as max_debt_value, avg(value) as avg_debt_value 
from debt_fact_table where value > '0';
<img width="1090" height="299" alt="image" src="https://github.com/user-attachments/assets/25ed5ce3-91a3-4a2b-a7cf-a67265fedf0a" />

# 10. Count total number of records in the dataset.
select count(*) as total_no_records from debt_fact_table;
<img width="948" height="259" alt="image" src="https://github.com/user-attachments/assets/1e159e94-4033-4c98-a87e-81dc9950aded" />

# Intermediate Level
# 1. Find the total debt for each country.
select c.country_name, sum(d.value) as total_debt from debt_fact_table d join country_table c 
on c.country_code = d.country_code group by c.country_name;
<img width="1090" height="294" alt="image" src="https://github.com/user-attachments/assets/a757599c-f737-4598-9b76-76697a55b667" />

# 2. Display the top 10 countries with the highest total debt.
select c.country_name, sum(d.value) as highest_total_debt, sum(d.value) as lowest_total_debt 
from debt_fact_table d join country_table c on c.country_code = d.country_code 
group by c.country_Name order by highest_total_debt desc limit 10;
<img width="1090" height="305" alt="image" src="https://github.com/user-attachments/assets/27b0dbd6-21a3-4e5e-a1ff-d79be5e768ec" />

select c.country_name, sum(d.value) as lowest_total_debt from debt_fact_table d join country_table c 
on c.country_code = d.country_codegroup by c.country_name order by lowest_total_debt asc limit 10;
<img width="1090" height="304" alt="image" src="https://github.com/user-attachments/assets/40f1277c-9425-4146-b891-7ca403892404" />

# 3. Find the average debt per country.
select c.country_name, avg(d.value) as average_debt from debt_fact_table d join country_table c 
on c.country_code = d.country_code group by c.country_name order by average_debt desc;
<img width="1090" height="304" alt="image" src="https://github.com/user-attachments/assets/c3516017-9585-4189-b4bc-42d312b7eb8c" />

# 4. Calculate total debt for each indicator.
select s.series_name, sum(d.value) as total_debt from debt_fact_table d join series_table s 
on s.series_code = d.series_code group by s.series_name;
<img width="1090" height="304" alt="image" src="https://github.com/user-attachments/assets/815db277-3f86-43da-be05-2767af711263" />

# 5. Identify the indicator contributing the highest total debt.
select s.series_name, sum(d.value) as highest_total_debt from debt_fact_table d join series_table s on s.series_code = d.series_code 
group by s.series_name having lowest_total_debt > '0' order by highest_total_debt desc limit 10;
<img width="1090" height="316" alt="image" src="https://github.com/user-attachments/assets/f7c5def0-8839-484f-9afb-f7c66d1582d6" />

select s.series_name, sum(d.value) as lowest_total_debt from debt_fact_table d join series_table s on s.series_code = d.series_code 
group by s.series_name having lowest_total_debt > '0' order by lowest_total_debt asc limit 10 ;
<img width="1090" height="302" alt="image" src="https://github.com/user-attachments/assets/d4a96008-ea3a-4919-98c6-f61f443b3bd3" />

# 6. Find the country with the lowest total debt.
select c.country_name, sum(d.value) as lowest_total_debt from debt_fact_table d join country_table c on c.country_code = d.country_code
group by c.country_name order by lowest_total_debt asc limit 1;
<img width="1090" height="317" alt="image" src="https://github.com/user-attachments/assets/4c1ab440-7f50-443b-9dca-7829eeaeaeaf" />

# 7. Calculate total debt for each country and indicator combination.
select c.country_name, s.series_name, sum(d.value) as total_debt from debt_fact_table d join country_table c on c.country_code = d.country_code
join series_table s on s.series_code = d.series_code group by c.country_name, s.series_name;
<img width="1090" height="322" alt="image" src="https://github.com/user-attachments/assets/862d3e57-67fd-4732-b265-8879fcf423d2" />


# 8. Count how many indicators each country has.
select c.country_name, Count(s.series_code) as total_indicators from country_series_table cs join country_table c on c.country_code = cs.country_code
join series_table s on s.series_code = cs.series_code group by cs.country_code;
<img width="1090" height="319" alt="image" src="https://github.com/user-attachments/assets/e0e596af-9059-4c93-ae8a-6cb115c7bcbe" />

select c.country_name, Count(s.series_code) as total_indicators from debt_fact_table d join country_table c on c.country_code = d.country_code
join series_table s on s.series_code = d.series_code group by d.country_code;
<img width="1090" height="303" alt="image" src="https://github.com/user-attachments/assets/4d816f6a-c699-4695-8b37-0208c1f1bf9a" />

# 9. Display countries whose total debt is above the global average.
with global_avg As
 ( Select avg(Value) as avg_value from debt_fact_table )
select c.country_Name, sum(d.value) as total_debt from debt_fact_table d join country_table c on c.country_code = d.country_code 
group by c.country_name Having total_debt > (select avg_value from global_avg);
<img width="1090" height="325" alt="image" src="https://github.com/user-attachments/assets/1829f4df-e582-40ef-a2d7-834a7dee8899" />


# 10. Rank countries based on total debt (highest to lowest).
select dense_rank() over ( order by Sum(d.value) desc) as debt_rank, c.country_Name, Sum(d.value) as total_debt 
from debt_fact_table d join country_table c on c.country_code = d.country_code group by c.country_name order by total_debt Desc;
<img width="1090" height="303" alt="image" src="https://github.com/user-attachments/assets/7978c90d-5d28-4277-95a3-ed1b07c8808e" />

# Advanced level
# 1. Find the top 5 indicators contributing most to global debt.
select s.Series_Name, sum(d.Value) as total_debt from debt_fact_table d join series_table s on s.Series_Code = d.Series_Code 
group by s.Series_Name order by total_debt Desc limit 5;
<img width="1090" height="336" alt="image" src="https://github.com/user-attachments/assets/2782cfff-8f46-473b-9f46-75c022fc8263" />

# 2. Calculate percentage contribution of each country to total global debt.
with global_total_debt as (
select sum(value) as total_global_debt from debt_fact_table)
select c.country_name, sum(d.value) as total_debt, cast((((sum(d.value)) / (select total_global_debt from global_total_debt)) * 100) as decimal (20,2)) as percentage_value 
from debt_fact_table d join country_table c on c.country_code = d.country_code group by c.country_name;
<img width="1090" height="337" alt="image" src="https://github.com/user-attachments/assets/1c75b105-26c3-4e7d-b4ee-02816d6f8728" />

# 3. Identify the top 3 countries for each indicator based on debt.
SELECT country_name, series_name, total_debt
FROM (
    SELECT c.country_name, s.series_name, SUM(d.value) AS total_debt,
        ROW_NUMBER() OVER ( PARTITION BY s.series_name ORDER BY SUM(d.value) DESC ) AS rank_num FROM debt_fact_table d 
        JOIN country_table c ON c.country_code = d.country_code JOIN series_table s ON s.series_code = d.series_code 
        GROUP BY c.country_name, s.series_name
) ranked
WHERE rank_num <= 3;
<img width="1090" height="411" alt="image" src="https://github.com/user-attachments/assets/4475beb1-ab62-436c-a35d-32b121388ef0" />

# 4. Find the difference between maximum and minimum debt for each country.
select c.country_name, max(d.value) as max_debt, min(d.value) as min_debt, (max(d.value) - min(d.Value) ) as dif_max_min 
from debt_fact_table d join country_table c on c.country_code = d.country_code where d.Value > '0' group by c.country_name;
<img width="1090" height="304" alt="image" src="https://github.com/user-attachments/assets/76ad6af5-7d1f-40c9-bf8c-619e3cdef648" />

# 5. Create a view for the top 10 countries with highest debt.
CREATE VIEW top_10_countries_highest_debt AS
SELECT c.country_name, SUM(d.value) AS highest_debt FROM debt_fact_table d JOIN country_table c ON c.country_code = d.country_code
GROUP BY c.country_name ORDER BY highest_debt DESC LIMIT 10;
select * from top_10_countries_highest_debt;
<img width="1090" height="354" alt="image" src="https://github.com/user-attachments/assets/761642c7-bba2-41bf-86cd-54b2d0e01cfc" />

# 6. Categorize countries into: High Debt Medium Debt Low Debt (based on thresholds)
SELECT c.country_name, SUM(d.value) AS total_debt,
    CASE 
        WHEN SUM(d.value) > 5000000000000 THEN 'High Debt'
        WHEN SUM(d.value) BETWEEN 1000000000000 AND 5000000000000 THEN 'Medium Debt'
        ELSE 'Low Debt'
    END AS debt_category
FROM debt_fact_table d JOIN country_table c ON c.country_code = d.country_code GROUP BY c.country_name ORDER BY total_debt DESC;
<img width="864" height="368" alt="image" src="https://github.com/user-attachments/assets/f918a2bc-563a-4b70-9bea-a5354966bb0f" />

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
<img width="1090" height="448" alt="image" src="https://github.com/user-attachments/assets/af2129ed-4e15-4af7-aa66-203edfe8116f" />

# 8. Find indicators where average debt is higher than overall average debt.
with global_avg as ( select cast(avg(value) as decimal(20,2)) as avg_value from debt_fact_table )
select s.series_name, cast(avg(d.value) as decimal(20,2)) as average_debt from debt_fact_table d join series_table s
 on s.series_code = d.series_code group by s.series_name having average_debt > (select avg_value from global_avg);
<img width="1090" height="333" alt="image" src="https://github.com/user-attachments/assets/8b847bad-2b7f-4931-81d7-0ad060487067" />

# 9. Identify countries contributing more than 5% of global debt. -> with - comm table exppresion (temp table)
with global_tot_debt as (select sum(value) as total_global_debt from debt_fact_table)
select c.country_name, sum(d.value) as total_debt, cast((((sum(d.value)) / (select total_global_debt from global_tot_debt)) * 100) 
as decimal(20,2)) as percentage_value 
from debt_fact_table d join country_table c on c.country_code = d.country_code 
group by c.country_name having percentage_value > 5 order by total_debt Desc;
<img width="1090" height="339" alt="image" src="https://github.com/user-attachments/assets/f7586d96-b2e8-49de-b522-191cba3474ae" />

# 10. Find the most dominant indicator (highest contribution) for each country.
WITH country_indicator_totals AS (
    SELECT c.country_name, s.series_name, SUM(d.value) AS total_value  FROM debt_fact_table d JOIN country_table c 
        ON c.country_code = d.country_code JOIN series_table s ON s.series_code = d.series_code 
        GROUP BY c.country_name, s.series_name ),
ranked_indicators AS ( SELECT *,  ROW_NUMBER() OVER ( PARTITION BY country_name ORDER BY total_value DESC ) AS rn 
FROM country_indicator_totals )
SELECT country_name, series_name, total_value AS highest_contribution FROM ranked_indicators WHERE rn = 1
ORDER BY highest_contribution DESC;
<img width="1090" height="371" alt="image" src="https://github.com/user-attachments/assets/160091a1-b60a-4ae4-b496-c71e07bdaa03" />




 


