import streamlit as st
import mysql.connector
import matplotlib.pyplot as plt
import plotly.express as px

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "Jagadeesan_V",
    database="international_debt_analysis"
)

cursor = conn.cursor()

st.set_page_config(layout = "wide", page_title= "International Debt Analysis")
st.title("International Debt Analysis")
col_1, col_2, col_3 = st.columns([1,1,1])

# top country high debt
with col_1: 
    with st.container(border= True):
        top_highest_debt_country_query = """select c.Country_Name, sum(d.Value) as highest_total_debt from debt_fact_table d join country_table c 
on c.Country_Code = d.Country_Code group by c.Country_Name order by highest_total_debt desc limit 10;"""
        cursor.execute(top_highest_debt_country_query)
        high_debt_result = cursor.fetchall()
        high_debt_country_list = [country_name[0] for country_name in high_debt_result]
        high_debt_value_list = [debt_value[1] for debt_value in high_debt_result]

# bar chart
        plt.figure(figsize=(10,10))
        high_debt_bar_graph = plt.bar(high_debt_country_list, high_debt_value_list,  color = 'green')
# padding=3 keeps the text from touching the bar
# fmt='%.1e' formats the huge numbers into scientific notation
        plt.bar_label(high_debt_bar_graph, rotation = 45, rotation_mode = 'default', padding=1, fmt='%.2f', fontsize=7, fontstyle = 'normal')
        plt.xticks(rotation = 45, ha = 'right')
        plt.title("Top country highest debt", fontsize = 20)
        plt.xlabel("Country Name", fontsize= 20)
        plt.ylabel("Debt Value", fontsize= 20)
        plt.ylim(0, float(max(high_debt_value_list)) * 1.25)
        st.pyplot(plt)

# line chart
        plt.figure(figsize=(13,5))
        plt.plot(high_debt_country_list, high_debt_value_list, marker = 'o')
        plt.xticks(rotation = 45, ha = 'right')
        plt.ylim(0, float(max(high_debt_value_list)) * 1.5)
        plt.title("Top country highest debt", fontsize = 20)
        plt.xlabel("Country Name",fontsize= 20)
        plt.ylabel("Debt Value",fontsize= 20)
        plt.grid()
        st.pyplot(plt)
        

with col_2: # top country lowest debt
    with st.container(border = True):
        top_lowest_debt_country_query = """select c.Country_Name, sum(d.Value) as lowest_total_debt from debt_fact_table d join country_table c 
on c.Country_Code = d.Country_Code group by c.Country_Name order by lowest_total_debt asc limit 10;"""
        cursor.execute(top_lowest_debt_country_query)
        low_debt_result = cursor.fetchall()
        low_debt_country_list = [country_name[0] for country_name in low_debt_result]
        low_debt_value_list = [debt_value[1] for debt_value in low_debt_result]

# bar chart
        plt.figure(figsize = (15,10))
        low_debt_bar = plt.bar(low_debt_country_list, low_debt_value_list, color = 'yellow')
        plt.bar_label(low_debt_bar, padding= 1, fmt= '%.2f', fontsize = 7)
        plt.xticks(rotation = 45, ha = 'right')
        plt.title("Top country lowest debt - bar chart", fontsize = 20)
        plt.xlabel("Country Name",fontsize= 20)
        plt.ylabel("Debt Value",fontsize= 20)
        plt.ylim(0, float(max(low_debt_value_list)) * 1.5)
        st.pyplot(plt)

# line chart
        plt.figure(figsize=(15,10))
        plt.plot(low_debt_country_list, low_debt_value_list, marker = 'o')
        plt.xticks(rotation = 45, ha = 'right')
        plt.title("Top country lowest debt - line chart", fontsize = 20)
        plt.xlabel("Country Name",fontsize= 20)
        plt.ylabel("Debt Value",fontsize= 20)
        plt.grid(True)
        st.pyplot(plt)
    
with col_3:
        with st.container(border= True):               
# top highest Debt distribution across different indicators
                indicator_wise_debt_destribution_query = """ select s.Series_Name, sum(d.Value) as debt_distribution from debt_fact_table d 
join series_table s on s.Series_Code = d.Series_Code group by s.Series_Name order by debt_distribution desc limit 10 """
                cursor.execute(indicator_wise_debt_destribution_query)
                high_debt_indicator_result = cursor.fetchall()
                series_list = [series_name[0] for series_name in high_debt_indicator_result]
                debt_value_list = [debt_value[1] for debt_value in high_debt_indicator_result]

                plt.figure(figsize=(20,10))
                indicator_debt = plt.bar(series_list, debt_value_list, color ='blue')
                plt.bar_label(indicator_debt, rotation = 45, padding= 1, fmt='%.2f', fontsize = 10, fontweight='bold')
                plt.xticks(rotation=40, ha='right', fontsize=10, fontweight='bold', family='calibri')
                plt.title("Top 10 Highest Debt with different Indicator", fontsize = 20)
                plt.xlabel("Indicator Name",fontsize= 20)
                plt.ylabel("Value",fontsize= 20)
                plt.ylim(0, float(max(debt_value_list)) * 1.5)
                plt.tight_layout()                     # automatic adjustment tool in Matplotlib -  tight_layout()
                st.pyplot(plt)

# top lowest Debt distribution across different indicators
                indicator_wise_debt_destribution_query = """ select s.Series_Name, sum(d.Value) as debt_distribution from debt_fact_table d 
join series_table s on s.Series_Code = d.Series_Code group by s.Series_Name order by debt_distribution asc limit 10 """
                cursor.execute(indicator_wise_debt_destribution_query)
                low_debt_indicator_result = cursor.fetchall()
                series_list = [series_name[0] for series_name in low_debt_indicator_result]
                debt_value_list = [debt_value[1] for debt_value in low_debt_indicator_result]

                plt.figure(figsize=(20,10))
                indicator_debt = plt.bar(series_list, debt_value_list, color ='red')
                plt.bar_label(indicator_debt,padding= -40, fmt='%.2f', fontsize = 10)
                plt.xticks(rotation=55, ha='right', fontsize=12, fontweight='bold', family='serif')
                plt.title("Top 10 Lowest Debt with different Indicator", fontsize = 20)
                plt.xlabel("Indicator Name",fontsize= 20)
                plt.ylabel("Value",fontsize= 20)
                plt.ylim(0, max(debt_value_list) * 30)
                plt.tight_layout()
                st.pyplot(plt)