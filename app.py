import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go




# Load data
df = pd.read_csv('L:\\GUVI_PYTHON\\project8\\cleaneddataset.csv') 
    
# Streamlit app
st.set_page_config(layout= "wide")
st.write("")
# st.title('Workers Population Analysis Dashboard')


#sidebar section1
with st.sidebar:
    select= option_menu("Main Menu",["Home", "Data Visualization and Exploration","Pie Charts and Histogram"])


if select == "Home":

        st.title("Industrial Human Resource Geo-Visualization")
        st.subheader("Resource Management")
        st.write("****About This Project:****")
        st.write("In India, the industrial classification of the workforce is essential to understand the distribution of the labor force across various sectors. The classification of main workers and marginal workers, other than cultivators and agricultural laborers, by sex and by section, division, and class, has been traditionally used to understand the economic status and employment trends in the country. However, the current data on this classification is outdated and may not accurately reflect the current state of the workforce. The aim of this study is to update the information on the industrial classification of the main and marginal workers, other than cultivators and agricultural laborers, by sex and by section, division, and class, to provide relevant and accurate data for policy making and employment planning.")
        st.write("****What can we do in this Project Insights:****")        
        st.write("****1.Merge all csv files and create a DataFrame****")
        st.write("****2.Data Exploration, Data Cleaning, Feature Engineering****")
        st.write("****3.Model Building and Model Testing****")
        st.write("****4.Use Natural Language Processing****")
  
      
       
   
        
       

       
# sidebar section2
if select == "Data Visualization and Exploration":
    # Select box for Group
    group = st.selectbox('Select Group:', df['Group'].unique())
    # Filter DataFrame based on selection
    df_filtered = df[df['Group'] == group]
    tab1, tab2= st.tabs(["Main Workers", "Marginal Workers"])

    with tab1:
        # method = st.radio("**Select the Analysis Method**",["Total Main Workers", "Main Workers (Rural vs Urban)", "Marginal Workers (Rural vs Urban)"])

        st.subheader(f'Total Main Workers in {group}')
        fig_total_main_workers = px.bar(df_filtered, x='India/States', y='Main Workers - Total -  Persons', color='India/States')
        st.plotly_chart(fig_total_main_workers)
        

        #Main Workers 
        col1,col2= st.columns(2)
        st.subheader(f'Main Workers (Rural vs Urban) in {group}')
        fig_main_workers_rural_urban = px.bar(df_filtered, x='India/States', 
                                    y=['Main Workers - Rural -  Persons', 'Main Workers - Urban -  Persons'],
                                    barmode='group', title="Main Workers - Rural vs Urban")
        st.plotly_chart(fig_main_workers_rural_urban)

        #Top 5 Main Workers states plots
        df['Total Workers'] = df['Main Workers - Rural -  Persons'] + df['Main Workers - Urban -  Persons']

        # Filter and sort the DataFrame to get the top 5 values
        df_top5 = df.nlargest(5, 'Total Workers')

        # Streamlit app
        st.title("Top 5 States by Main Workers - Rural vs Urban")

        # Main Workers
        fig_main_workers_rural_urban = px.bar(df_top5, x='India/States', 
                                            y=['Main Workers - Rural -  Persons', 'Main Workers - Urban -  Persons'],
                                            barmode='group', title="Top 5 States Main Workers - Rural vs Urban")

        # Show the figure in Streamlit
        st.plotly_chart(fig_main_workers_rural_urban)


    with tab2:
        
        
        st.subheader(f'Total Main Workers in {group}')
        fig_total_main_workers = px.bar(df_filtered, x='India/States', y='Main Workers - Total -  Persons', color='India/States')
        st.plotly_chart(fig_total_main_workers)

        #Marginal Workers 
        col1,col2= st.columns(2)
        st.subheader(f'Marginal Workers (Rural vs Urban) in {group}')
        fig_marginal_workers_rural_urban = px.bar(df_filtered, x='India/States', 
                                        y=['Marginal Workers - Rural -  Persons', 'Marginal Workers - Urban -  Persons'],
                                        barmode='group', title="Marginal Workers - Rural vs Urban")
        st.plotly_chart(fig_marginal_workers_rural_urban)

        # Top 5 State Marginal Workers Plots
        df['Total Marginal Workers'] = df['Marginal Workers - Rural -  Persons'] + df['Marginal Workers - Urban -  Persons']

        # Filter and sort the DataFrame to get the top 5 values
        df_top5_marginal = df.nlargest(5, 'Total Marginal Workers')

        # Streamlit app
        st.title("Top 5 States by Marginal Workers - Rural vs Urban")

        # Marginal Workers
        fig_marginal_workers_rural_urban = px.bar(df_top5_marginal, x='India/States', 
                                                y=['Marginal Workers - Rural -  Persons', 'Marginal Workers - Urban -  Persons'],
                                                barmode='group', title="Top 5 States by Marginal Workers - Rural vs Urban",
                                                labels={
                                                    "value": "Number of Workers",
                                                    "variable": "Category"
                                                })

        
        st.plotly_chart(fig_marginal_workers_rural_urban) 


# Pie charts
# sidebar section3
if select == "Pie Charts and Histogram":
    tab1, tab2, tab3= st.tabs(["Pie Charts", "Histogram", "Stacked Bar Plot"])

    with tab1:       
        
        # Summing up the columns to get the total for main and marginal workers
        main_workers = df[['Main Workers - Total - Males', 'Main Workers - Total - Females']].sum()
        marginal_workers = df[['Marginal Workers - Total - Males', 'Marginal Workers - Total - Females']].sum()

        # Creating the pie chart with Plotly
        fig_pie = go.Figure()

        fig_pie.add_trace(go.Pie(
            labels=main_workers.index,
            values=main_workers.values,
            name='Main Workers',
            domain=dict(x=[0.0, 0.5])
        ))

        fig_pie.add_trace(go.Pie(
            labels=marginal_workers.index,
            values=marginal_workers.values,
            name='Marginal Workers',
            domain=dict(x=[0.5, 1.0])
        ))

        fig_pie.update_layout(
            title='Distribution of Total Main and Marginal Workers by Gender',
            annotations=[dict(text='Main Workers', x=0.2, y=0.5, font_size=15, showarrow=False),
                        dict(text='Marginal Workers', x=0.8, y=0.5, font_size=15, showarrow=False)]
        )

        #Pie chart with gender wise visualization
        #Creating the pie chart with Plotly
        main_workers = df[['Main Workers - Rural - Males','Main Workers - Rural - Females','Main Workers - Urban - Males', 'Main Workers - Urban - Females']].sum()
        marginal_workers = df[['Marginal Workers - Rural - Males', 'Marginal Workers - Rural - Females','Marginal Workers - Urban - Males','Marginal Workers - Urban - Females']].sum()
        fig_pie2 = go.Figure()

        fig_pie2.add_trace(go.Pie(
            labels=main_workers.index,
            values=main_workers.values,
            name='Main Workers',
            domain=dict(x=[0.0, 0.5])
        ))

        fig_pie2.add_trace(go.Pie(
            labels=marginal_workers.index,
            values=marginal_workers.values,
            name='Marginal Workers',
            domain=dict(x=[0.5, 1.0])
        ))

        fig_pie2.update_layout(
            title='Distribution of Rural & Urban Main and Marginal Workers by Gender',
            annotations=[dict(text='Main Workers', x=0.2, y=0.5, font_size=15, showarrow=False),
                        dict(text='Marginal Workers', x=0.8, y=0.5, font_size=15, showarrow=False)]
        )
            
        
        # Streamlit app
        st.title('Distribution of Rural & Urban Workers by Gender')
        
        st.plotly_chart(fig_pie)
        st.plotly_chart(fig_pie2)
        



    with tab2:
        
        # Histogram
        # Creating the histogram with Plotly
        fig_cluster_hist = go.Figure()

        fig_cluster_hist.add_trace(go.Histogram(
            x=df['Cluster_Label'],
            name='Cluster_Label Distribution',
            opacity=0.75
        ))

        fig_cluster_hist.update_layout(
            title='Distribution of Cluster Labels',
            xaxis_title='Cluster Label',
            yaxis_title='Count',
            legend_title='Cluster'
        )

        # Streamlit app
        st.title('Distribution of Cluster Labels')
        st.plotly_chart(fig_cluster_hist)

        df_long = df.melt(
            id_vars=['Cluster_Label'],
            value_vars=['Main Workers - Rural - Males', 'Main Workers - Rural - Females',
                        'Main Workers - Urban - Males', 'Main Workers - Urban - Females'],
            var_name='Worker_Type', 
            value_name='Count'
        )

        # Add a Gender column based on the Worker_Type column
        df_long['Gender'] = df_long['Worker_Type'].apply(lambda x: 'Male' if 'Males' in x else 'Female')

        # Add a Location column based on the Worker_Type column
        df_long['Location'] = df_long['Worker_Type'].apply(lambda x: 'Rural' if 'Rural' in x else 'Urban')

        # Aggregate the data for stacked bar plotting
        df_aggregated = df_long.groupby(['Cluster_Label', 'Location', 'Gender'])['Count'].sum().reset_index()

        # Create Streamlit app
        st.title('Distribution of Cluster Labels by Gender and Location')

        # Display stacked bar chart
        fig_stacked_bar = px.bar(
            df_aggregated,
            x='Cluster_Label',
            y='Count',
            color='Gender',
            facet_col='Location',
            labels={'Count': 'Number of Workers', 'Cluster_Label': 'Cluster Label'},
            title='Distribution of Cluster Labels by Gender and Location'
        )

        st.plotly_chart(fig_stacked_bar)



    with tab3:

        #Donut Chart
        # Extract the clusters and values
        clusters = df['Cluster_Label']
        
        # Use `hole` to create a donut-like pie chart
        fig_donut = go.Figure(data=[go.Pie(labels=clusters,hole=.3)])
        title = 'Donut Chart' 

         # Melt the DataFrame to have a long format for easier plotting
        df_long = df.melt(id_vars=['Cluster_Label'],
                        value_vars=['Main Workers - Total - Males', 'Main Workers - Total - Females',
                                    'Marginal Workers - Total - Males', 'Marginal Workers - Total - Females'],
                        var_name='Worker_Type', value_name='Count')

        # Add a Gender column based on the Worker_Type column
        df_long['Gender'] = df_long['Worker_Type'].apply(lambda x: 'Male' if 'Males' in x else 'Female')

        # Aggregate the data for stacked bar plotting
        df_aggregated = df_long.groupby(['Cluster_Label', 'Gender'])['Count'].sum().reset_index()

        # Create a stacked bar chart with Plotly Express
        fig_stacked_bar = px.bar(
            df_aggregated,
            x='Cluster_Label',
            y='Count',
            color='Gender',
            labels={'Count': 'Number of Workers', 'Cluster_Label': 'Cluster Label'},
            title='Distribution of Cluster Labels by Gender'
        )

        st.title('Cluster Label Donut Chart')
        st.plotly_chart(fig_donut)        
        st.plotly_chart(fig_stacked_bar)   









# ...................................................................................................................#
# ...................................................................................................................#
# ...................................................................................................................#
# Additional Analysis
#st.subheader('Additional Analysis')
#st.write(df_filtered.describe())
 



