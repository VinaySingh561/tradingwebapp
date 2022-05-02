#!/usr/bin/env python
# coding: utf-8

# In[3]:


#! pip install streamlit


# In[4]:


#! pip install pillow


# # Stock Market dashboard
# ## Import libraries

# In[5]:


import streamlit as st
import pandas as pd
from PIL import Image


# ## Add a title and an image
# 

# In[18]:


st.write("""
# Stock market web application
**Visually** showing data
""")
image = Image.open("Opening.jpg")
st.image(image, use_column_width = True)


# ## Create a sidebar header

# In[19]:


st.sidebar.header("User Input")


# ## Create a function to get the users input

# In[29]:


def get_input():
    start_date = st.sidebar.text_input("Start_date",  "2021-05-01")
    end_date = st.sidebar.text_input("End_date",  "2022-05-01")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol


# ### create a function to get the company name

# In[30]:


def get_company_name(symbol):
    if symbol == 'AMZN':
        return "Amazon"
    elif symbol == 'TSLA':
        return "TSLA"
    elif symbol == "GOOG":
        return "Google"
    else:
        "None"


# ### Create a function to get the company data and the proper time

# In[34]:


def get_data(symbol, start, end):
    
    ## Load the data
    if symbol.upper()== "AMZN":
        df= pd.read_csv("AMZN.csv")
    elif symbol.upper()== "TSLA":
        df= pd.read_csv("TSLA.csv")
    elif symbol.upper()== "GOOG":
        df= pd.read_csv("GOOG.csv")    
    else:
        df = pd.DataFrame(columns = ["Date", "Open", "High", "Low", "Close","Volume"])
            
    ## Get date range       
    start  = pd.to_datetime(start)
    end = pd.to_datetime(end)
    
    # Set the start and end index rows both to 0
    start_row = 0
    end_row = 0
    
    # Find the start date and end date
    for i in range(len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break
    for j in range(len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df)-1-j
            break   
            
     # set the date as index
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))
    
    return df.iloc[start_row: end_row+1 , :]




# ### Get the user input

# In[35]:


start, end , symbol = get_input()


# In[36]:


## get the data
df= get_data(symbol,start, end)


# In[37]:


## get the comapny name
company_name = get_company_name(symbol.upper())


# ### Display the close price

# In[39]:


st.header(company_name + "Close Price\n")
st.line_chart(df['Close'])

st.header(company_name + "Close Price\n")
st.line_chart(df['Volume'])


# In[ ]:




