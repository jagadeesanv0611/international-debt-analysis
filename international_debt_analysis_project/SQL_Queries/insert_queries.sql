import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jagadeesan_V"
)
cursor = conn.cursor()


#use database
cursor.execute("USE international_debt_analysis;")

country_table_query = "Insert IGNORE into country_table (Country_Code, Country_Name, Region, Income_Group, Currency_Unit, Special_Notes) values (%s, %s, %s, %s, %s, %s);"
cursor.executemany(country_table_query, ids_country_data_frame.values.tolist())
conn.commit()

series_table_query = "Insert IGNORE into series_table (Series_Code, Series_Name, Short_definition, Source, Periodicity, General_comments) values (%s, %s, %s, %s, %s, %s);"
cursor.executemany(series_table_query, ids_series_data_frame.values.tolist())
conn.commit()

debt_fact_table_query = "Insert IGNORE into debt_fact_table (Country_Code, Series_Code, Year, value) values (%s, %s, %s, %s);"
cursor.executemany(debt_fact_table_query, ids_all_countries_data_frame.values.tolist())
conn.commit()

country_series_table_query = "Insert IGNORE into country_series_table (Country_Code, Series_Code, Description) values (%s, %s, %s);"
cursor.executemany(country_series_table_query, country_series_data_frame.values.tolist())
conn.commit()

foot_note_table_query = "Insert IGNORE into foot_note_table (Country_Code, Series_Code, Year, Description) values (%s, %s, %s, %s);"
cursor.executemany(foot_note_table_query, ids_foot_note_data_frame.values.tolist())
conn.commit()

# Seesion time out - to prevent 30 sec disconnect
cursor.execute("SET SESSION wait_timeout = 600;")
cursor.execute("SET SESSION net_read_timeout = 600;")
cursor.execute("SET SESSION net_write_timeout = 600;")