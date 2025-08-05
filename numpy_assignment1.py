#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr=np.array([1,2,3,6,4,5])
reversearray=arr[::-1]
print(reversearray)


# In[5]:


array1=np.array([[1,2,3],[2,4,5],[1,2,3]])
flatten_array=array1.flatten()
print(flatten_array)


# In[8]:


arr1=np.array([[1,2],[3,4]])
arr2=np.array([[1,2],[3,4]])
np.array_equal(arr1,arr2)


# In[9]:


gfg=np.matrix('[4,1,9;12,3,1;4,5,6]')
gfg.sum()


# In[10]:


gfg.sum(axis=0)


# In[11]:


gfg.sum(axis=1)


# In[12]:


n_array=np.array([[55,25,15],[30,44,2],[11,45,77]])
np.trace(n_array)


# In[13]:


np.linalg.eig(n_array)


# In[14]:


np.linalg.det(n_array)


# In[15]:


np.linalg.inv(n_array)


# In[16]:


p=[[1,2],[2,3]]
q=[[4,5],[6,7]]
np.dot(p,q)


# In[17]:


np.cov(p)


# In[20]:


np.cov(q)


# In[21]:


x=np.array([[2,3,4],[3,2,9]]);
y=np.array([[1,5,0],[5,10,3]]);
np.inner(x,y)


# In[22]:


np.outer(x,y)


# In[ ]:




