import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jagadeesan_V"
)
cursor = conn.cursor()

#use database
cursor.execute("USE international_debt_analysis;")

country_table_query = "Insert IGNORE into country_table (country_code, country_name, region, income_group, currency_unit, special_notes) values (%s, %s, %s, %s, %s, %s);"
cursor.executemany(country_table_query, ids_country_data_frame.values.tolist())
conn.commit()

series_table_query = "Insert IGNORE into series_table (series_code, series_name, short_definition, source, general_comments) values (%s, %s, %s, %s, %s);"
cursor.executemany(series_table_query, ids_series_data_frame.values.tolist())
conn.commit()

debt_fact_table_query = "Insert IGNORE into debt_fact_table (country_code, series_code, year, value) values (%s, %s, %s, %s);"
cursor.executemany(debt_fact_table_query, ids_all_countries_data_frame.values.tolist())
conn.commit()

country_series_table_query = "Insert IGNORE into country_series_table (country_code, series_code, description) values (%s, %s, %s);"
cursor.executemany(country_series_table_query, country_series_data_frame.values.tolist())
conn.commit()

foot_note_table_query = "Insert IGNORE into foot_note_table (country_code, series_code, year, description) values (%s, %s, %s, %s);"
cursor.executemany(foot_note_table_query, ids_foot_note_data_frame.values.tolist())
conn.commit()
