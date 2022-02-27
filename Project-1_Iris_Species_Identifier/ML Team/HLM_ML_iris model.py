#!/usr/bin/env python
# coding: utf-8

# # Import section

# In[1]:


from pandas import *
from numpy import *
from seaborn import *
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import *
from sklearn.linear_model import *
from sklearn import metrics
from sklearn import preprocessing


# # Data Gathering

# In[2]:


ds= get_dataset_names()


# In[3]:


pip install category_encoders


# In[4]:


ds


# In[5]:


ds=load_dataset("iris")


# In[6]:


ds


# In[7]:


ds.isnull()


# In[8]:


X=ds.drop("species", axis=1)
X


# In[9]:


Y=ds.species


# In[16]:


Y
encoder= preprocessing.LabelEncoder()
ds["species"]= encoder.fit_transform(ds["species"])
ds["species"].unique()
Y=ds.species


# In[17]:


train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.2, random_state=3)


# In[18]:


ds


# In[19]:


model=KNeighborsRegressor()


# In[20]:


model.fit(train_x,train_y)


# In[21]:


model.predict(test_x)
model.score(test_x,test_y)


# In[25]:


model.predict([[1.2, 3.0, 2.1, 1]])


# In[ ]:




