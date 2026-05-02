#sql - coonnector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Jagadeesan_V"
    )
cursor = conn.cursor()

#creating database
cursor.execute("CREATE DATABASE IF NOT EXISTS international_debt_analysis;")

#use database
cursor.execute("USE international_debt_analysis;")

#create country table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS country_table (
               country_code VARCHAR(3) NOT NULL PRIMARY KEY,
               country_name VARCHAR(50) NOT NULL,
               region VARCHAR(100) NOT NULL,
               income_group VARCHAR(100) NOT NULL,
               currency_Unit VARCHAR(100) NOT NULL,
               special_notes TEXT           
     );               
""")
conn.commit()

#create series table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS series_table (
               series_code VARCHAR(30) NOT NULL PRIMARY KEY,
               series_name TEXT,
               short_definition TEXT,
               source TEXT,
               general_comments TEXT
     );               
""")
conn.commit()

#create debt_fact_table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS debt_fact_table (
               debt_fact_id INT AUTO_INCREMENT PRIMARY KEY,
               country_code VARCHAR(3) NOT NULL,
               series_code VARCHAR(30) NOT NULL,
               year INT,
               value DECIMAL(20,2),
               FOREIGN KEY (country_code) REFERENCES country_table(country_code),
               FOREIGN KEY (series_code) REFERENCES series_table(series_code)
     );
""")
conn.commit()

#create country_series_table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS country_series_table (
               country_series_id INT AUTO_INCREMENT PRIMARY KEY,
               country_code VARCHAR(3) NOT NULL,
               series_code VARCHAR(30) NOT NULL,
               description TEXT,
               FOREIGN KEY (country_code) REFERENCES country_table(country_code),
               FOREIGN KEY (series_code) REFERENCES series_table(series_code)
     );
""")
conn.commit()

#create Foot_note_table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS foot_note_table (
               foot_note_id INT AUTO_INCREMENT PRIMARY KEY,
               country_code VARCHAR(3) NOT NULL,
               series_code VARCHAR(30) NOT NULL,
               year INT,
               description TEXT,
               FOREIGN KEY (country_code) REFERENCES country_table(country_code),
               FOREIGN KEY (series_code) REFERENCES series_table(series_code)
     );
""")
conn.commit()


