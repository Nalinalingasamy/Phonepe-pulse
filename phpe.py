#cloning data from github
#powershell or gitbash--> 'git clone "link from github"' 


#importing libraries
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import mysql.connector as mysql
import pymysql
import pandas as pd
import plotly.express as px
import json
import os 
import git
# !pip install streamlit_option_menu
# !pip install GitPython

#connecting to Mysql & creating "Phonepe_cpsproject" database
mydb=pymysql.connect(host='127.0.0.1',
                user='root',
                password='Viyan@15',
                port=3306,
                database="Phonepe_cpsproject")
cur=mydb.cursor()
#cur.execute("create database Phonepe_cpsproject")

# Setting up page configuration

st.title(":violet[PHONEPE PULSE DATA VISUALIZATION AND EXPLORATION]")
#creating sidebar for option menu
with st.sidebar:
           video_file = open('C:\\Users\\NANDHU\\Downloads\\pulse-video.mp4', 'rb')
           video1 = video_file.read()
           st.video(video1)
           st.header(":orange[**WELCOME TO DASHBOARD**]")
           st.write("The User-Friendly Tool created by Nalina Lingasamy for capstone project in Data Science course")          
           selected = option_menu("Menu", ["Home","About Phonepe data","Top Charts","Explore Data","Geo Visual"], 
                icons=["house","graph-up-arrow","bar-chart-line", "exclamation-circle"],
                menu_icon= "menu-button-wide",
                default_index=0,
                styles={"nav-link": {"font-size": "15px", "text-align": "left", "margin": "-2px", "--hover-color": "#8F9CAE"},
                        "nav-link-selected": {"background-color": "#6F36AD"}})
           

if selected == "Home":

    st.write("PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
    st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    st.write(" ")
    st.markdown("## :orange[Phonepe is now everywhere!!!]")
    

    col1,col2 = st.columns([1,1],gap="medium")
    with col1:
        image1 = Image.open(r"C:\\Users\\NANDHU\\Desktop\\Pulse-Insight-Header-Pulse-Bytes-Size.png")
        st.image(image1,width= 305)
    with col2:
        image2 = Image.open(r"C:\\Users\\NANDHU\\Desktop\\Split-Bills-Icon.png")
        st.image(image2,width= 250)

    col3,col4 = st.columns([1,1],gap="medium")
    with col3:
        image3 = Image.open(r"C:\\Users\\NANDHU\\Desktop\\Small-Icon-1.png")
        st.image(image3,width= 305)
    with col4:
        image4 = Image.open(r"C:\Users\NANDHU\Desktop\Designing.png")
        st.image(image4,width= 305)


if selected == "About Phonepe data":

    st.header(":violet[INTRODUCTION]")
    st.write('''The Indian digital payments story has truly captured the world's imagination. 
                From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones,
                mobile internet and state-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government. 
                Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India.
                When we started, we were constantly looking for granular and definitive data sources on digital payments in India. 
                PhonePe Pulse is our way of giving back to the digital payments ecosystem.''')

    st.write('')
    st.header(":violet[PhonePe Pulse Data: Insights for India]")
    st.write('')

    st.subheader(":violet[Key Dimensions :]")
    st.write('- State - All States in India')
    st.write('- Year -  2018 to 2023')
    st.write('- Quarter - Q1 (Jan to Mar), Q2 (Apr to June), Q3 (July to Sep), Q4 (Oct to Dec)')

    st.subheader(":violet[Aggregated Transaction:]")
    st.write('Transaction data broken down by type of payments at state level.')
    st.write('- Recharge & bill payments')
    st.write('- Peer-to-peer payments')
    st.write('- Merchant payments')
    st.write('- Financial Services')
    st.write('- Others')

    st.subheader(":violet[Aggregated User:]")
    st.write('Users data broken down by devices at state level.')
    col1,col2,col3,col4, col5, col6 = st.columns(6)
    with col1:
        st.write(':small_blue_diamond: Apple')
        st.write(':small_blue_diamond: Asus')
        st.write(':small_blue_diamond: Coolpad')
        st.write(':small_blue_diamond: Gionee')
        st.write(':small_blue_diamond: HMD Global')
    with col2:
        st.write(':small_blue_diamond: Huawei')
        st.write(':small_blue_diamond: Infinix')
        st.write(':small_blue_diamond: Lava')
        st.write(':small_blue_diamond: Lenovo')
        st.write(':small_blue_diamond: Lyf')
    with col3:
        st.write(':small_blue_diamond: Micromax')
        st.write(':small_blue_diamond: Motorola')
        st.write(':small_blue_diamond: OnePlus')
        st.write(':small_blue_diamond: Oppo')
        st.write(':small_blue_diamond: Realme')
    with col4:
        st.write(':small_blue_diamond: Samsung')
        st.write(':small_blue_diamond: Tecno')
        st.write(':small_blue_diamond: Vivo')
        st.write(':small_blue_diamond: Xiaomi')
        st.write(':small_blue_diamond: Others')

    st.subheader(":violet[Map Transaction:]")
    st.write('- Total number of transactions at the state / district level.')
    st.write('- Total value of all transactions at the state / district level.')

    st.subheader(":violet[Map User:]")
    st.write('- Total number of registered users at the state / district level.')
    st.write('- Total number of app opens by these registered users at the state / district level.')

    st.subheader(":violet[Top Transaction:]")
    st.write('Explore the most number of the transactions happened for a selected Year-Quarter combination')
    st.write('- Top 10 States')
    st.write('- Top 10 Districts')
    st.write('- Top 10 Pincodes')

    st.subheader(":violet[Top User:]")
    st.write('Explore the most number of registered users for a selected Year-Quarter combination')
    st.write('- Top 10 States')
    st.write('- Top 10 Districts')
    st.write('- Top 10 Pincodes')


if selected == "Top Charts":
    st.markdown("## :violet[Top Charts]")
    Type = st.selectbox("**Type**", ("Transactions", "Users"))
    colum1,colum2= st.columns([1,1],gap="large")
    with colum1:
        Year = st.slider("**Year**", min_value=2018, max_value=2023)
    with colum2:
        Quarter = st.slider("Quarter", min_value=1, max_value=4)
    
    st.info(
            """
                Here we can get insights like :
            - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on PhonePe.
            - Top 10 State, District, Pincode based on Total PhonePe users and their app opening frequency.
            - Top 10 mobile brands and its percentage based on how many people use PhonePe.
            """,icon="🔍"
            )

# Top Charts - TRANSACTIONS    
    if Type == "Transactions":
            
                # PIE CHART - TOP PAYMENT TYPE
            st.markdown("## :violet[Top Payment Type]")
            cur.execute(f'''select Transaction_type, sum(Transaction_count) as Total_Transactions,
                        sum(Transaction_amount) as Total_amount from agg_trans 
                        where year= {Year} and quarter = {Quarter} group by transaction_type
                        order by Transaction_type''')
            df = pd.DataFrame(cur.fetchall(), columns=['Transaction_type','Total_Transactions','Total_amount'])

            fig1=px.pie(df,
                        values= "Total_Transactions",
                        names="Transaction_type",
                        title='Transaction_types vs Total_Transactions',
                        color_discrete_sequence=px.colors.sequential.Plasma,
                        hover_data=['Total_Transactions'],
                        labels={'Total_Transactions':'Total_Transactions'}
                        )
            
            fig1.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig1,use_container_width=True)

            

            #Bar chart - Top 10 states by transaction
            st.markdown("### :violet[State_wise]")
            cur.execute(f'''select state, sum(Transaction_count) as Total_Transactions_Count,
                        sum(Transaction_amount) as Total_Amount from agg_trans 
                        where year = {Year} and quarter = {Quarter} group by state 
                        order by Total_Amount desc limit 10''')
            df = pd.DataFrame(cur.fetchall(), columns=['State', 'Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                            names='State',
                            title='Top 10 states by Transaction',
                            color_discrete_sequence=px.colors.sequential.thermal,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

            #Bar chart - Top 10 districts by Transaction
            st.markdown("### :violet[District_wise]")
            cur.execute(f'''select district , sum(Count) as Total_Count, sum(Amount) as Total_Amount
                        from map_trans where year = {Year} and quarter = {Quarter} 
                        group by district order by Total_Amount desc limit 10''')
            df = pd.DataFrame(cur.fetchall(), columns=['District', 'Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                            names='District',
                            title='Top 10 districts by Transaction',
                            color_discrete_sequence=px.colors.sequential.deep,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
             #Bar chart - Top 10 pincode by Transaction
            st.markdown("### :violet[Pincode_wise]")
            cur.execute(f'''select pincode, sum(Transaction_count) as Total_Transactions_Count,
                        sum(Transaction_amount) as Total from top_trans
                        where year = {Year} and quarter = {Quarter} 
                        group by pincode order by Total desc limit 10''')
            df = pd.DataFrame(cur.fetchall(), columns=['Pincode', 'Transactions_Count','Total_Amount'])
            fig = px.pie(df, values='Total_Amount',
                            names='Pincode',
                            title='Top 10 pincode area by Transaction',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)


    # Top Charts - USERS          
    if Type == "Users":

        #BAR CHART for Top 10 Brands by Users:
        st.markdown("### :violet[Brands]")
        if Year in [2022,2023] and Quarter in [2,3,4]:
                st.markdown("#### Sorry No Data to Display for this Year and Qtr")
        else:
            cur.execute(f'''select Brands, sum(Count) as Total_Count, avg(Percentage)*100 as Avg_Percentage 
                        from agg_user where year = {Year} and quarter = {Quarter}
                        group by Brands order by Total_Count desc limit 10''')
            df = pd.DataFrame(cur.fetchall(), columns=['Brand', 'Total_Users','Avg_Percentage'])
            fig = px.bar(df,title='Top 10 Brands by Users',
                            x="Brand",
                            y="Total_Users",
                            orientation='v',
                            color='Avg_Percentage',
                            color_continuous_scale=px.colors.sequential.Aggrnyl)
            st.plotly_chart(fig,use_container_width=True)   

        #BAR CHART- Top 10 districts by users
        st.markdown("### :violet[District]")
        cur.execute(f'''select district, sum(RegisteredUser) as Total_Users, sum(AppOpens) as Total_Appopens 
                    from map_user where year = {Year} and quarter = {Quarter} group by district 
                    order by Total_Users desc limit 10''')
        df = pd.DataFrame(cur.fetchall(), columns=['District', 'Total_Users','Total_Appopens'])
        df.Total_Users = df.Total_Users.astype(float)
        fig = px.bar(df,
                        title='Top 10 Districts by Users',
                        x="District",
                        y="Total_Users",
                        orientation='v',
                        color='Total_Users',
                        color_continuous_scale=px.colors.sequential.dense)
        st.plotly_chart(fig,use_container_width=True)

        #PIE CHART -    
        st.markdown("### :violet[State]")
        cur.execute(f'''select state, sum(Registereduser) as Total_Users, 
                    sum(AppOpens) as Total_Appopens from map_user 
                    where year = {Year} and quarter = {Quarter} group by state 
                    order by Total_Users desc limit 10''')
        df = pd.DataFrame(cur.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])

        fig1 = px.bar(df,
                      title='Top 10 States by Users',
                      x= "State",
                      y="Total_Users",
                      orientation='v',
                      color='Total_Users',
                      color_continuous_scale=px.colors.sequential.dense
                      )
        st.plotly_chart(fig1,use_container_width=True)


# MENU 3 - EXPLORE DATA
if selected == "Explore Data":
    Type = st.selectbox("**Type**", ("Transactions", "Users"))
    colum1,colum2= st.columns([1,1],gap="large")
    with colum1:
        Year = st.slider("**Year**", min_value=2018, max_value=2023)
    with colum2:
        Quarter = st.slider("Quarter", min_value=1, max_value=4)

# EXPLORE DATA - TRANSACTIONS
    if Type == "Transactions":
                
        # BAR CHART TRANSACTIONS - DISTRICT WISE DATA            
        st.markdown("# ")
        st.markdown("## :violet[Select any State to explore:]")
        selected_state = st.selectbox("",
                                ('Andaman-&-nicobar-islands','Andhra-pradesh','Arunachal-pradesh','Assam','Bihar',
                                'Chandigarh','Chattisgarh','Dadra-&-nagar-haveli-&-daman-&-diu','Delhi','Goa','Gujarat','Haryana',
                                'Himachal-pradesh','Jammu-&-Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep',
                                'Madhya-pradesh','Maharashtra','Manipur','Meghalaya','Mizoram',
                                'Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim',
                                'Tamil-nadu','Telangana','Tripura','Uttar-pradesh','Uttarakhand','West-Bengal'),index=30)
            
        cur.execute(f'''select State, District,year,quarter, sum(count) as Total_Transactions,
                    sum(amount) as Total_amount from map_trans 
                    where year = {Year} and quarter = {Quarter} and State = '{selected_state}' 
                    group by State, District,year,quarter order by state,district''')

        df1 = pd.DataFrame(cur.fetchall(), columns=['State','District','Year','Quarter',
                                                            'Total_Transactions','Total_amount'])
        fig = px.bar(df1,
                        title=f"Trans Count in Districts of {selected_state}",
                        x="District",
                        y="Total_Transactions",
                        orientation='v',
                        color='Total_Transactions',
                        color_continuous_scale=px.colors.sequential.Sunsetdark)
        st.plotly_chart(fig,use_container_width=True)

        fig1 = px.bar(df1,
                        title=f"Trans Amount in Districts of {selected_state}",
                        x="District",
                        y="Total_amount",
                        orientation='v',
                        color='Total_amount',
                        color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig1,use_container_width=True)


#EXPLORE DATA - USERS      
    if Type == "Users":

    # Overall State Data - TOTAL APPOPENS - INDIA MAP
        st.header(":violet[Overall State Data]")
        cur.execute(f'''select state, sum(RegisteredUser) as Total_Users, 
                    sum(AppOpens) as Total_Appopens from map_user 
                    where year = {Year} and quarter = {Quarter} group by state order by state''')
        df1 = pd.DataFrame(cur.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
        df2 = pd.read_csv(r"C:\\Users\\NANDHU\\Downloads\\Statenames.csv")
        df1.Total_Appopens = df1.Total_Appopens.astype(float)
        df1.State = df2

    # BAR CHART TOTAL UERS - DISTRICT WISE DATA 
        st.markdown("## :violet[Select any State to explore:]")
        selected_state = st.selectbox("",
                                ('Andaman-&-nicobar-islands','Andhra-pradesh','Arunachal-pradesh','Assam','Bihar',
                                'Chandigarh','Chattisgarh','Dadra-&-nagar-haveli-&-daman-&-diu','Delhi','Goa','Gujarat','Haryana',
                                'Himachal-pradesh','Jammu-&-Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep',
                                'Madhya-pradesh','Maharashtra','Manipur','Meghalaya','Mizoram',
                                'Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim',
                                'Tamil-nadu','Telangana','Tripura','Uttar-pradesh','Uttarakhand','West-Bengal'),index=30)

        cur.execute(f'''select State,year,quarter,District,sum(Registereduser) as Total_Reg_Users, 
                    sum(AppOpens) as Total_Appopens from map_user 
                    where year = {Year} and quarter = {Quarter} and state = '{selected_state}' 
                    group by State, District,year,quarter order by state,district''')

        df = pd.DataFrame(cur.fetchall(), columns=['State','year', 'quarter', 'District', 'Total_reg_Users','Total_Appopens'])
        df.Total_reg_Users = df.Total_reg_Users.astype(int)

        fig = px.bar(df,
                        title=f"Reg Users in Districts of {selected_state}",
                        x="District",
                        y="Total_reg_Users",
                        orientation='v',
                        color='Total_reg_Users',
                        color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)
        
        fig1 = px.bar(df,
                        title=f"App Opens in Districts of {selected_state}",
                        x="District",
                        y="Total_Appopens",
                        orientation='v',
                        color='Total_Appopens',
                        color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig1,use_container_width=True)

if selected == "Geo Visual":  
        Type = st.selectbox("**Type**", ("Transactions", "Users"))
        colum1,colum2= st.columns([1,1],gap="large")
        with colum1:
            Year = st.slider("**Year**", min_value=2018, max_value=2023)
        with colum2:
            Quarter = st.slider("Quarter", min_value=1, max_value=4)  

    # Overall State Data - TRANSACTIONS AMOUNT - INDIA MAP 
        if Type == "Transactions": 
            sel=st.radio("Select Type:",("Amount","Count"))
            if sel == "Amount":
                st.markdown("## :violet[Overall Transaction Amount]")
                cur.execute(f'''select state, sum(count) as Total_Transactions, sum(amount) as Total_amount 
                            from map_trans where year = {Year} and quarter = {Quarter} 
                            group by state order by state''')
                df1 = pd.DataFrame(cur.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
                df2 = pd.read_csv(r"C:\\Users\\NANDHU\\Downloads\\Statenames.csv")
                df1.State = df2

                fig = px.choropleth(df1,geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Total_amount',
                            color_continuous_scale='viridis')

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig,use_container_width=True)
    # Overall State Data - TRANSACTIONS COUNT - INDIA MAP
            if sel == "Count":
                st.markdown("## :violet[Overall Transaction Count]")
                cur.execute(f'''select state, sum(count) as Total_Transactions, sum(amount) as Total_amount
                            from map_trans where year = {Year} and quarter = {Quarter} 
                            group by state order by state''')
                df1 = pd.DataFrame(cur.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
                df2 = pd.read_csv(r"C:\\Users\\NANDHU\\Downloads\\Statenames.csv")
                df1.Total_Transactions = df1.Total_Transactions.astype(int)
                df1.State = df2

                fig = px.choropleth(df1,geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Total_Transactions',
                            color_continuous_scale='plasma')

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig,use_container_width=True)
            
         
        #Overall State Data - RegisteredUser
        if Type == "Users": 
            st.markdown("## :violet[Overall State - Registered Users]")
            cur.execute(f'''select state, sum(RegisteredUser)
                        from map_user where year = {Year} and quarter = {Quarter} 
                        group by state order by state''')
            df1 = pd.DataFrame(cur.fetchall(),columns= ['State', 'RegisteredUser'])
            df2 = pd.read_csv(r"C:\\Users\\NANDHU\\Downloads\\Statenames.csv")
            df1.RegisteredUser = df1.RegisteredUser.astype(int)
            df1.State = df2

            fig = px.choropleth(df1,geojson=r"https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color='RegisteredUser',
                        color_continuous_scale='rdpu')

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig,use_container_width=True)
                
