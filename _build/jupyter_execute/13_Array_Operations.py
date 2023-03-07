#!/usr/bin/env python
# coding: utf-8

# # Indexing

# In[1]:


import numpy as np

arr=np.arange(10)
arr.resize(4,2)

arr


# In[2]:


arr[1,1]


# In[3]:


arr[3,:] # first row every element


# In[4]:


a= arr[:,0] # first column every element

a

a[0]


# In[5]:


a= arr[:,:-1]  #first column - every element as a seperate array

a
a[0]


# # Fancy indexing with Another Array

# In[6]:


arr_i = np.array([[0,1],[0,1],[1,0],[1,0]], dtype=bool)
arr_i


# In[7]:


arr[arr_i]=100 # replace with 100 where arr_i is True

arr


# # Operations on Arrays
# 
# Mathematical operations performed elementwise. We can do addition, deleting, multiplication, and division on arrays. 
# 
# **Both arrays have to be of the same shape!**

# # Addition

# In[8]:


arr_b= arr+1
arr_b


# In[9]:


arr+arr_b


# # Multiplication

# In[10]:


arr_c= arr*2
arr_c


# In[11]:


arr_c*arr


# # Subtraction

# In[12]:


arr_c-arr_b


# # Division

# In[13]:


arr_c/arr_b


# # Boolean

# In[14]:


arr_c>20

