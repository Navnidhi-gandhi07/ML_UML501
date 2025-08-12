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





data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

df = pd.DataFrame(data)
df.to_csv("employees.csv", index=False)

import pandas as pd
df = pd.read_csv("employees.csv")

print("Shape ", df.shape)

print(df.info())

print(df.describe())

print(df.head())

print(df.tail(3))

average= df["Salary"].mean()
total = df["Bonus"].sum()
youngest = df["Age"].min()
highest = df["Rating"].max()

print("Average", average)
print("Total", total)
print("Youngest ", youngest)
print(, highest)

sortdf = df.sort_values(by="Salary", ascending=False)

print(sortdf)
print("\nMissing Values ")
print(df.isnull().sum())

df.rename(columns={"Employee_ID": "ID"}, inplace=True)
print(df.head())

print(df[df["Years_of_Experience"] > 5])

print(df[df["Department"] == "IT"])
df["Tax"] = df["Salary"] * 0.1

print(df)

df.to_csv("modified_employees.csv", index=False)

from google.colab import files
uploaded = files.upload()
df = pd.read_csv('Iris.csv')
print(df.head())





