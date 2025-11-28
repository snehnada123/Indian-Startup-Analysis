import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(layout='wide',page_title='Startup Analysis')
df=pd.read_csv('startup_cleaned.csv')
df['Date']=pd.to_datetime(df['Date'],errors='coerce',dayfirst=True)
df['Year']=df['Date'].dt.year

def load_investor_details(investor):
    st.title(investor)
    
    #load recent 5 investments
    last5_df=df[df['Investors'].str.contains(investor)].head()[['Date','Startup','Vertical','City','Round','Amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)
    
    col1,col2=st.columns(2)
    with col1:
        #Top investments of all time
        st.subheader('Biggest Investments')
        top_df=df[df['Investors'].str.contains(investor)].groupby('Startup')['Amount'].sum().sort_values(ascending=False)
        # st.dataframe(top_df) 
        fig,ax=plt.subplots()
        ax.bar(top_df.index,top_df.values)
        st.pyplot(fig)
    
        #Stages invested in
        st.subheader('Stages Invested in')
        stage=df[df['Investors'].str.contains(investor)].groupby('Round')['Amount'].sum()
        fig2,ax2=plt.subplots()
        ax2.pie(stage,labels=stage.index)
        st.pyplot(fig2)
        
        #Year wise investments
        st.subheader("Year wise investments")
        df['Year']=df['Date'].dt.year
        year_investment=df[df['Investors'].str.contains(investor)].groupby('Year')['Amount'].sum()
        fig4,ax4=plt.subplots()
        ax4.plot(year_investment.index,year_investment.values)
        st.pyplot(fig4)
        
    with col2:
        #All verticals invested
        verticals=df[df['Investors'].str.contains(investor)].groupby('Vertical')['Amount'].sum()
        st.subheader('Sectors Invested')
        fig1,ax1=plt.subplots()
        ax1.pie(verticals,labels=verticals.index,autopct="%0.01f")
        st.pyplot(fig1)
        
        
        st.subheader('Cities invested')
        city=df[df['Investors'].str.contains(investor)].groupby('City')['Amount'].sum()
        fig3,ax3=plt.subplots()
        ax3.pie(city,labels=city.index)
        st.pyplot(fig3)

    #To show similar investors 
    st.subheader('Similar Investors')
    invest=df.groupby(['Investors','Vertical'])
    total_investment=invest['Amount'].sum().sort_values(ascending=False)
    vert = df[df['Investors'].str.contains(investor)].groupby('Vertical')['Amount'].sum().sort_values(ascending=False).head(1)
    verticals=list(vert.index)
    similar_investors=total_investment.loc[total_investment.index.get_level_values('Vertical').isin(verticals)]
    st.dataframe(similar_investors)
        
def load_overall_analysis():
    st.title('Overall Analysis')
    total=round(df['Amount'].sum())
    maxi=df.groupby('Startup')['Amount'].max().sort_values(ascending=False).head(1).values[0]
    average=df.groupby('Startup')['Amount'].sum().mean()
    num=df['Startup'].nunique()
    df['Month']=df['Date'].dt.month
    col1,col2,col3,col4=st.columns(4)  
    
    with col1:
        #total invested amount
        st.metric('Total',str(total)+' Cr')
    
    with col2:
        #Maximum amount
        st.metric('Max',str(maxi)+' Cr')
        
    with col3:
        #total ticket size
        st.metric('Average',str(round(average))+' Cr')
    
    with col4:
        #total funded_startups
        st.metric('Funded Startups',str(num))
        
    
    st.header('MoM graph')
    selected_option=st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':
        temp_df=df.groupby(['Year','Month'])['Amount'].sum().reset_index()
    else:
        temp_df=df.groupby(['Year','Month'])['Amount'].count().reset_index()
    temp_df['x_axis']=temp_df['Month'].astype('str')+"-"+temp_df['Year'].astype('str')
    
    
    fig5,ax5=plt.subplots()
    ax5.plot(temp_df['x_axis'],temp_df['Amount'])
    st.pyplot(fig5)
    
    
def load_startup_details(startup):
    st.title(startup)
    
    
    st.metric("Industry",df[df['Startup']==startup]['Vertical'].values[0])
        
    st.metric("Sub Industry",df[df['Startup']==startup]['SubVertical'].values[0])
    
    st.metric("City",df[df['Startup']==startup]['City'].values[0])
        
        
    st.subheader("Rounds")
    st.dataframe(df[df['Startup']=='Shuttl'][['Round','Investors','Date']])
    
    st.subheader("Similar Companies")
    temp_df=df[(df['Vertical'] == df[df['Startup']==startup]['Vertical'].values[0]) & (df['Startup']!=startup)]['Startup']
    st.dataframe(temp_df)
    
    
option=st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
        load_overall_analysis()
        
elif option == 'Startup':
    selected_startup=st.sidebar.selectbox('Select Startup',df['Startup'].unique().tolist())
    btn1=st.sidebar.button("Find Startup Details")
    if btn1:
        load_startup_details(selected_startup)
else:
     selected_investor=st.sidebar.selectbox('Select Investor',set(df['Investors'].str.split(",").sum()))
     btn2=st.sidebar.button("Find Investor Details")
     
     if btn2:
         load_investor_details(selected_investor)