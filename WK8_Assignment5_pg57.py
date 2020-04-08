#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 


# In[15]:


names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,95,77,78,99] 
bsdegrees = [1,1,0,0,1] 
msdegrees = [2,1,0,0,0] 
phddegrees = [0,1,0,0,0]


# In[16]:


GradeList = zip(names,grades, bsdegrees, msdegrees,phddegrees)


# In[17]:


df = pd.DataFrame(data=GradeList,columns=['Names','Grades', 'BS', 'MS' , 'PhD']) 


# In[18]:


df['Grades'].count()  
df['Grades'].mean()  
df['Grades'].std()
df['Grades'].min()
df['Grades'].max()
df['Grades'].quantile(.25)
df['Grades'].quantile(.5)
df['Grades'].quantile(.75) 


# In[19]:


df


# In[20]:


df.loc[df['PhD']==0].count()

