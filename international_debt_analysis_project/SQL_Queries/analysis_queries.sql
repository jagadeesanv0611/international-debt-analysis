# SQL Analysis:

# SQL Analytical Questions (30)

# Basic Queries

# 1. Retrieve all distinct country names from the dataset.
select Country_Name from country_table;

# 2. Count the total number of countries available.
select count(Country_Name) as total_no_of_countries from country_table;

# 3. Find the total number of indicators present.
select count(Series_Name) as total_no_of_indicators from series_table;

# 4. Display the first 10 records of the dataset.
select c.Country_Name, s.Series_Name, d.Year, d.Value from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code join series_table s on s.Series_Code = d.Series_Code limit 10 ;

# 5. Calculate the total global debt.
select sum(Value) as total_global_debt from debt_fact_table;

# 6. List all unique indicator names.
select Series_Name as Unique_indicator_name from series_table;

# 7. Find the number of records for each country.
select c.Country_Name, count(*) as no_of_records from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name order by no_of_records Desc;

# 8. Display all records where debt is greater than 1 billion USD.
select * from debt_fact_table where value > '1000000000' order by Value Asc;

# 9. Find the minimum, maximum, and average debt values.
select min(Value) as min_debt_value, max(Value) as max_debt_value, avg(Value) as avg_debt_value from debt_fact_table;

# 10. Count total number of records in the dataset.
select count(*) as total_no_records from debt_fact_table;


# Intermediate Level

# 1. Find the total debt for each country.
select c.Country_Name, sum(d.Value) as total_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name;

# 2. Display the top 10 countries with the highest total debt.
select c.Country_Name, sum(d.Value) as highest_total_debt, sum(d.Value) as lowest_total_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name order by highest_total_debt desc limit 10;

select c.Country_Name, sum(d.Value) as lowest_total_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name order by lowest_total_debt asc limit 10;

# 3. Find the average debt per country.
select c.Country_Name, avg(d.value) as average_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name order by average_debt desc;

# 4. Calculate total debt for each indicator.
select s.Series_Name, sum(d.Value) as total_debt from debt_fact_table d join series_table s on s.Series_Code = d.Series_Code group by s.Series_Name;

# 5. Identify the indicator contributing the highest total debt.
select s.Series_Name, sum(d.Value) as highest_total_debt from debt_fact_table d join series_table s on s.Series_Code = d.Series_Code group by s.Series_Name order by highest_total_debt desc limit 10;

select s.Series_Name, sum(d.Value) as lowest_total_debt from debt_fact_table d join series_table s on s.Series_Code = d.Series_Code group by s.Series_Name having lowest_total_debt > 0 order by lowest_total_debt asc limit 10 ;

# 6. Find the country with the lowest total debt.
select c.Country_Name, sum(d.Value) as lowest_total_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name order by lowest_total_debt asc limit 1;

# 7. Calculate total debt for each country and indicator combination.
select c.Country_Name, s.Series_Name, sum(d.value) as total_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code join series_table s on s.Series_Code = d.Series_Code group by c.Country_Name, s.Series_Name;

# 8. Count how many indicators each country has.
select c.Country_Name, Count(s.Series_Code) as total_indicators from country_series_table cs join country_table c on c.Country_Code = cs.Country_Code join series_table s on s.Series_Code = cs.Series_Code group by cs.Country_Code;

# 9. Display countries whose total debt is above the global average.
with global_avg As ( Select avg(Value) as avg_value from debt_fact_table ) select c.Country_Name, sum(d.value) as total_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name Having total_debt > (select avg_value from global_avg);

# 10. Rank countries based on total debt (highest to lowest).
select dense_rank() over ( order by Sum(d.Value) desc) as debt_rank, c.Country_Name, Sum(d.Value) as total_debt from debt_fact_table d join country_table c on c.Country_Code = d.Country_Code group by c.Country_Name order by total_debt Desc;
