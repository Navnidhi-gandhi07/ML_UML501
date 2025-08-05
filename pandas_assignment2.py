#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
data={
    'tid':[1,2,3,4,5,6,7,8,9,10],
    'Refund':['yes','no','no','yes','no','no','yes','no','no','no'],
    'Marital status':['single','Married','single','Married','Divorced','Married','Divorced','single','Married','single'],
    'Taxable income':['125K','100K','70K','120K','95K','60K','220K','85K','75K','90K'],
    'cheat':['no','no','no','no','yes','no','no','yes','no','yes']
}
df=pd.DataFrame(data)


# In[8]:


print(df)


# In[11]:


print(df.loc[0])


# In[12]:


print(df.loc[4])


# In[13]:


print(df.loc[7])


# In[14]:


print(df.loc[8])


# In[16]:


df.iloc[3:7]


# In[17]:


df.iloc[4:8,2:4]


# In[19]:


df.iloc[:,1:4]


# In[ ]:





# In[ ]:




