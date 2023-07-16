import streamlit as st
import pandas as pd
import openai_helper
st.title('financial data extraction')

# column layout
col1, col2 = st.columns([3,2]) # 3 portion out of 5 will display the text and 2 portion out of 5 will display the table( here we consider the screen is 5 units)
#create an empty dataframe
financial_data_df = pd.DataFrame({
        "Measure": ["Company Name","Stock Symbol","Revenue","Net Income","EPS"],
        "Values": ["", "", "", "", ""] } )

with col1:
    st.title('Data Extraction tool')
    news_article = st.text_area('Paste your financial news article here', height= 300)
    # pass the vale again empty data frame i.e financial_data_df
    if st.button('Extract'):

        financial_data_df=openai_helper.extract_financial_data(news_article)

with col2 :
    st.markdown("<br/>" * 5, unsafe_allow_html= True ) # create 5 lines of vertical spaces ,we did this for align the table with tool
    st.dataframe(financial_data_df,column_config= {"Measure": st.column_config.Column(width=150),
                     "Values": st.column_config.Column(width=150)
                 },                                               # we change the width
                 hide_index= True)