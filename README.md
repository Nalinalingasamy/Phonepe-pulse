# Phonepe-pulse
# Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly 
  The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics. The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.
  
# Introduction
   PhonePe has become one of the most popular digital payment platforms in India, with millions of users relying on it for their day-to-day transactions. The app is known for its simplicity, user-friendly interface, and fast and secure payment processing. It has also won several awards and accolades for its innovative features and contributions to the digital payments industry.

We create a web app to analyse the Phonepe transaction and users depending on various Years, Quarters, States, and Types of transaction and give a Geographical and Geo visualization output based on given requirements.

## Developer Guide
#  Tools installed
--> Virtual Studio code

--> Jupyter notebook.

--> Python 3.11.0 or higher.

--> SQL Workbench

--> Git

# Approach:

### Data extraction: 
  Clone the Github using scripting to fetch the data from the Phonepe pulse Github repository and store it in a suitable format such as CSV or JSON.
### Data transformation: 
  Use a scripting language such as Python, along with libraries such as Pandas, to manipulate and pre-process the data. This may include cleaning the data, handling missing values, and transforming the data into a format suitable for analysis and visualization.
### Database insertion: 
  Use the "mysql-connector-python" library in Python to connect to a MySQL database and insert the transformed data using SQL commands.
### Dashboard creation:
  Use the Streamlit and Plotly libraries in Python to create an interactive and visually appealing dashboard. Plotly's built-in geo map functions can be used to display the data on a map and Streamlit can be used to create a user-friendly interface with multiple dropdown options for users to select different facts and figures to display.
### Data retrieval: 
  Use the "mysql-connector-python" library to connect to the MySQL database and fetch the data into a Pandas dataframe. Use the data in the dataframe to update the dashboard dynamically.
# Deployment: 
  Ensure the solution is secure, efficient, and user-friendly. Test the solution thoroughly and deploy the dashboard publicly, making it accessible to users.

# Learning outcomes of this project:
### Data extraction and processing: 
  Learning how to use Clone Github to extract data from a repository and pre-process the data using Python libraries such as Pandas.
### Database management: 
  Use a relational database such as MySQL to store data and retrieve it efficiently for analysis and visualization.
Visualization and dashboard creation: To use libraries such as Streamlit and Plotly to create interactive and visually appealing dashboards for data visualization.
### Geo visualization: 
  Create and display data on a map using Plotly's built-in geo map functions.
### Dynamic updating: 
  Create a dashboard that dynamically updates based on the latest data in a database.
### Project development and deployment:
  Develop a comprehensive and user-friendly solution, from data extraction to dashboard deployment. Also learn how to test and deploy the solution to ensure it is secure, efficient, and user-friendly.

## THE MAIN COMPONENTS OF DASHBOARD ARE

1. GEO-VISUALIZATION

2. TRANSACTIONS ANALYSIS

3. USERS ANALYSIS

4. TOP STATES DATA


### 1. Geo-Visualization: 
  The India map shows the Total Transactions of PhonePe in both state wide and District wide.It comes with zoom option and on hover displays the content related to that particular state or district.The main functions I have used to create this map are (User can give year and quarter input to show how the data changed over time)

1. Plotlys scatter_geo for plotting districts along with the conent    

2. Plotlys coropleth for drawing the states in India map

   
### 2. Transactions Analysis: 
  The Transactions data mainly contains the total Transactions count and total amount in each state and district, I have used different graphs available in plotly to represent this data

1. State-wise study
The above bar graph shows the increasing order of PhonePe Transactions according to the states of India, 
Here we can observe the top states with the highest Transaction by looking at graph

2. District-wise study
User can observe how transactions are happening in districts of a selected state.We can observe the 
leading distric in a state

3. Year-wise study   
We can observe the states with total transactions in particular mode in the selected year

4. Overall Analysis
To show how the transactions drastically increased with time


### 3. User Data Analysis: 
  The Users data mainly contains the Registered Users count and App openings via different mobile brands in each state and district,I have used different graphs available in plotly to represent this data

1. State-wise study
User can observe how the App Openings are growing and how Registered users are growing in a state

2. District-wise study
User can observe how App Openings are happening in districts of a selected state

3. Year-wise study   
User can observe the top leading brands in a particular state in given year

4. Overall Analysis
We can see that the Registered Users and App openings are increasing year by year


### 4. Top States Data:

1. States with top Registered users 

2. States with top Total Amount Transacted

3. States with highest Trabsactions count

4. States with top app openings
