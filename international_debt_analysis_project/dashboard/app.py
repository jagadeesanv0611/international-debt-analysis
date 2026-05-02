import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "wide", page_title= "International Debt Analysis")
st.title("International Debt Analysis")

conn =  mysql.connector.connect(
     host="localhost",
     user="root",
     password= "Jagadeesan_V",
     database="international_debt_analysis"
)
cursor = conn.cursor()

# top 10 country high debt and lowest debt
with st.container(border= True):
        top_highest_debt_country_query = """select c.country_name, sum(d.value) as highest_total_debt from debt_fact_table d 
        join country_table c on c.country_code = d.country_code group by c.country_name order by highest_total_debt desc limit 10;"""
        cursor.execute(top_highest_debt_country_query)
        high_debt_result = cursor.fetchall()
        high_debt_country_list = [country_name[0] for country_name in high_debt_result]
        high_debt_country_value_list = [debt_value[1] for debt_value in high_debt_result]

        top_lowest_debt_country_query = """select c.country_name, sum(d.value) as lowest_total_debt from debt_fact_table d 
        join country_table c  on c.country_code = d.country_code group by c.country_name order by lowest_total_debt asc limit 10;"""
        cursor.execute(top_lowest_debt_country_query)
        low_debt_result = cursor.fetchall()
        low_debt_country_list = [country_name[0] for country_name in low_debt_result]
        low_debt_country_value_list = [debt_value[1] for debt_value in low_debt_result]

        col_1, col_2 = st.columns([1,1])
        with col_1:
             top_high_debt_country_bar_fig = px.bar(x= high_debt_country_list, y=high_debt_country_value_list, 
                                                   color_discrete_sequence=['#1f77b4'])
             top_high_debt_country_bar_fig.update_layout( xaxis_title = "Country Name",
                                          yaxis_title = "Debt Value",
                                          title = "Top 10 countries highest debt", title_x = 0.5,
                                          xaxis=dict( showline=True, linecolor='black', linewidth=2 ),
                                          yaxis=dict( showline=True, linecolor='black',  linewidth=2, tickformat="$~s" ) )
             st.plotly_chart(top_high_debt_country_bar_fig, use_container_width=True)

        with col_2:
             top_low_debt_country_bar_fig = px.bar(x= low_debt_country_list, y=low_debt_country_value_list, 
                                                  color_discrete_sequence=["#f01212"])
             top_low_debt_country_bar_fig.update_layout( xaxis_title = "Country Name",
                                          yaxis_title = "Debt Value",
                                          title = "Top 10 countries lowest debt", title_x = 0.5,
                                          xaxis=dict( showline=True, linecolor='black', linewidth=2 ),
                                          yaxis=dict( showline=True, linecolor='black',  linewidth=2, tickformat="$~s" ) )
             st.plotly_chart(top_low_debt_country_bar_fig, use_container_width=True)


# Top 15 country percentage of global debt:
with st.container(border=True):
        top_country_percentage_global_debt_query = """with global_total_debt as 
        (select sum(value) as total_global_debt from debt_fact_table)
select c.country_name, sum(d.value) as total_debt, cast((((sum(d.value)) / (select total_global_debt from global_total_debt)) * 100) 
as decimal (20,2)) as percentage_value from debt_fact_table d join country_table c on 
c.country_code = d.country_code group by c.country_name order by percentage_value desc limit 15;"""
        cursor.execute(top_country_percentage_global_debt_query)
        top_country_percentage_result = cursor.fetchall()
        top_country_name = [country_name[0] for country_name in top_country_percentage_result]
        percentage_value = [percentage_value[2] for percentage_value in top_country_percentage_result]
        top_country_percentage_bar_fig = px.bar(x= top_country_name, y= percentage_value,
                                                color_discrete_sequence=["#e28914"] )
        top_country_percentage_bar_fig.update_layout( xaxis_title = "Country Name",
                                                     yaxis_title = "percentage of Global Debt",
                                                     title = "Percentage contribution to Global Debt - Top 15",
                                                     xaxis=dict( showline=True, linecolor='black',  linewidth=2, 
                                                                showgrid= True, gridcolor= 'lightgrey'),
                                                      yaxis=dict( showline=True, linecolor='black',  linewidth=2,
                                                                 showgrid= True, gridcolor= 'lightgrey'),
                                                        title_x = 0.5        )
        st.plotly_chart(top_country_percentage_bar_fig, use_container_width = True)


# Top countries - annual debt heatmap (2000 - 2032)
with st.container(border=True):
      top_country_annual_debt_query = """SELECT  c.country_name, d.year, SUM(d.value) AS total_debt_value FROM debt_fact_table d 
JOIN country_table c ON c.country_code = d.country_code 
JOIN ( SELECT country_code FROM debt_fact_table GROUP BY country_code ORDER BY SUM(value) DESC LIMIT 10) AS top_countries
ON d.country_code = top_countries.country_code GROUP BY c.country_name, d.year ORDER BY d.year ASC;"""

      heatmap_country_annual_debt_dataframe = pd.read_sql(top_country_annual_debt_query, conn)
      heatmap_country_annual_debt_dataframe_pivot = heatmap_country_annual_debt_dataframe.pivot(index='country_name', 
                                                                                  columns='year', 
                                                                                  values='total_debt_value')
      heatmap_country_annual_debt_fig = px.imshow( heatmap_country_annual_debt_dataframe_pivot,
                                                   text_auto=True, 
                                                   color_continuous_scale='YlOrRd',
                                                   aspect="auto")
      heatmap_country_annual_debt_fig.update_layout(
                                                      height = 500,
                                                      width = 500,
                                                      xaxis_title="Year",
                                                      yaxis_title= "Country Name",
                                                      title="Top countries - annual debt heatmap (2000 - 2032)",
                                                      title_x=0.5)
      st.plotly_chart(heatmap_country_annual_debt_fig, use_container_width=True)


# Countries by debt category
with st.container(border=True):
      country_debt_category_query = """SELECT c.country_name, SUM(d.value) AS total_debt FROM debt_fact_table d 
                          JOIN country_table c ON c.country_code = d.country_code GROUP BY c.country_name; """
      country_debt_category_dataframe = pd.read_sql(country_debt_category_query, conn)

      def assign_category(value):
          if value > 5000000000000:
              return 'High Debt (>5T)'
          elif 1000000000000 <= value <= 5000000000000:
              return 'Medium Debt (1T - 5T)'
          else:
              return 'Low Debt (<1T)'

      country_debt_category_dataframe['debt_category'] = country_debt_category_dataframe['total_debt'].apply(assign_category)
      country_debt_category_dataframe_counts = country_debt_category_dataframe['debt_category'].value_counts().reset_index()
      country_debt_category_dataframe_counts.columns = ['debt_category', 'count']
      country_debt_category_dataframe_fig = px.bar(country_debt_category_dataframe_counts, x='debt_category', y='count', 
                                                   color='debt_category',
        color_discrete_map={
            'High Debt (>5T)': '#e74c3c',
            'Medium Debt (1T - 5T)': '#f39c12',
            'Low Debt (<1T)': '#2ecc71'
        },
        text_auto=True,
        title="Countries by Debt Category")
      country_debt_category_dataframe_fig.update_layout(xaxis_title="Debt Category",
                                 yaxis_title="Number of Countries",
                                 template="plotly_white",
                                 showlegend=False,
                                 title_x=0.5       )
      st.plotly_chart(country_debt_category_dataframe_fig, use_container_width=True)


# trends bet year and value
with st.container(border= True):
        trends_bet_year_value_query = """select year, sum(value) as total_debt_value from debt_fact_table
                                         group by year order by year asc;"""
        trends_bet_year_value_dataframe = pd.read_sql(trends_bet_year_value_query, conn)
        trends_bet_year_value_fig = px.area( trends_bet_year_value_dataframe, x='year', y='total_debt_value',
                                              title="Global Debt Trend (2000 - 2032)",
                                              markers=True )
        trends_bet_year_value_fig.update_traces( line_color='#2980b9', 
                                                 fillcolor='rgba(41, 128, 185, 0.1)' 
                                                  )
        trends_bet_year_value_fig.update_layout( xaxis_title="Year",
                                                 yaxis_title="Total Debt ",
                                                 template="plotly_white",
                                                 title_x=0.5,
                                                 yaxis=dict(tickformat="$~s") 
                                                 )
        st.plotly_chart(trends_bet_year_value_fig, use_container_width=True)


# top 10 countries trend
with st.container(border=True):
        top_trends_country_year_value_query = """ SELECT c.country_name, d.year, SUM(d.value) AS debt_value 
        FROM debt_fact_table d JOIN country_table c ON c.country_code = d.country_code 
        JOIN ( SELECT country_code FROM debt_fact_table GROUP BY country_code ORDER BY SUM(value) DESC LIMIT 10 ) 
        AS top ON d.country_code = top.country_code GROUP BY c.country_name, d.year ORDER BY d.year ASC; """
        top_trends_country_year_value_dataframe = pd.read_sql(top_trends_country_year_value_query, conn)
        top_trends_country_year_value_fig = px.line(top_trends_country_year_value_dataframe,
                                                    x='year', y='debt_value', color='country_name',
                                                    title="Debt Trends for Top 10 Countries")
        top_trends_country_year_value_fig.update_layout(xaxis_title = "Year",
                                                        yaxis_title = "Debt Value",
                                                        title_x=0.5,
                                                        yaxis=dict(tickformat="$~s") )
        st.plotly_chart(top_trends_country_year_value_fig, use_container_width=True)
        
   
# top 10 series high debt 
with st.container(border= True):
        indicator_wise_high_debt_distribution_query = """ select s.series_name as indicator_name, sum(d.value) as 
        total_high_debt_distribution from debt_fact_table d join series_table s on s.series_code = d.series_code group by 
        indicator_name order by total_high_debt_distribution desc limit 10 ;"""
        indicator_wise_high_debt_distribution_dataframe = pd.read_sql(indicator_wise_high_debt_distribution_query, conn)
        indicator_wise_high_debt_distribution_fig = px.pie(indicator_wise_high_debt_distribution_dataframe, 
                                                      values='total_high_debt_distribution',
                                                      names='indicator_name',
                                                      title= " Top 10 Indicators with High Debt Distribution")
        indicator_wise_high_debt_distribution_fig.update_layout(title_x = 0.5)
        st.plotly_chart(indicator_wise_high_debt_distribution_fig, use_container_width= True)
       
     
# top 10 series low debt
with st.container(border= True):
        indicator_wise_low_debt_distribution_query = """ select s.series_name as indicator_name, sum(d.value) as 
        total_low_debt_distribution from debt_fact_table d join series_table s on s.series_code = d.series_code 
        group by indicator_name having total_low_debt_distribution > '0' order by total_low_debt_distribution asc limit 10 """
        indicator_wise_low_debt_distribution_dataframe = pd.read_sql(indicator_wise_low_debt_distribution_query, conn)
        indicator_wise_low_debt_distribution_fig = px.pie(indicator_wise_low_debt_distribution_dataframe,
                                                         values = 'total_low_debt_distribution',
                                                         names= 'indicator_name',
                                                         title = " Top 10 Indicators with Low Debt Distribution")
        indicator_wise_low_debt_distribution_fig.update_layout(title_x = 0.5)
        st.plotly_chart(indicator_wise_low_debt_distribution_fig, use_container_width= True)       
