#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
df=pd.read_csv("C:\\Users\\shubham_kumar\\Desktop\\HistoricalQuotes.csv",parse_dates=["Date"],index_col="Date")
df


# In[6]:


df["2019-11-13":"2019-11-11"]


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()


# In[43]:


#generate frequency 
df=pd.date_range(start="08/11/2019",periods=20,freq='B')
df

