#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 


# In[5]:


location = 'C:\\Users\\nchin\\DataViz\\Week8_files\\gradedata.csv'


# In[6]:


df = pd.read_csv(location)


# In[8]:


df.take(np.random.permutation(len(df))[:500]) 


# In[ ]:




