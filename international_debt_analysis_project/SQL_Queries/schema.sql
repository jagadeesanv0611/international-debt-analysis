#sql - connector
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jagadeesan_V"
)
cursor = conn.cursor()

#creating database
cursor.execute("CREATE DATABASE IF NOT EXISTS international_debt_analysis;")

#use database
cursor.execute("USE international_debt_analysis;")

#create country table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS country_table (
               Country_Code VARCHAR(3) NOT NULL PRIMARY KEY,
               Country_Name VARCHAR(50) NOT NULL,
               Region VARCHAR(100) NOT NULL,
               Income_Group VARCHAR(100) NOT NULL,
               Currency_Unit VARCHAR(100) NOT NULL,
               Special_Notes TEXT           
     );               
""")
conn.commit()

#create series table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS series_table (
               Series_Code VARCHAR(30) NOT NULL PRIMARY KEY,
               Series_Name TEXT,
               Short_definition TEXT,
               Source TEXT,
               Periodicity VARCHAR(10),
               General_comments TEXT
     );               
""")
conn.commit()

#create debt fact table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS debt_fact_table (
               Debt_Fact_Id INT AUTO_INCREMENT PRIMARY KEY,
               Country_Code VARCHAR(3) NOT NULL,
               Series_Code VARCHAR(30) NOT NULL,
               Year INT,
               Value DECIMAL(20,2),
               FOREIGN KEY (Country_Code) REFERENCES country_table(Country_Code),
               FOREIGN KEY (Series_Code) REFERENCES series_table(Series_Code)
     );
""")
conn.commit()

#create country series table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS country_series_table (
               Country_Series_Id INT AUTO_INCREMENT PRIMARY KEY,
               Country_Code VARCHAR(3) NOT NULL,
               Series_Code VARCHAR(30) NOT NULL,
               Description TEXT,
               FOREIGN KEY (Country_Code) REFERENCES country_table(Country_Code),
               FOREIGN KEY (Series_Code) REFERENCES series_table(Series_Code)
     );
""")
conn.commit()

#create foot note table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS foot_note_table (
               Foot_Note_Id INT AUTO_INCREMENT PRIMARY KEY,
               Country_Code VARCHAR(3) NOT NULL,
               Series_Code VARCHAR(30) NOT NULL,
               Year INT,
               Description TEXT,
               FOREIGN KEY (Country_Code) REFERENCES country_table(Country_Code),
               FOREIGN KEY (Series_Code) REFERENCES series_table(Series_Code)
     );
""")
conn.commit()
