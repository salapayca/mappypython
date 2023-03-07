#!/usr/bin/env python
# coding: utf-8

# # Reshaping Arrays

# In[1]:


# changing a shape

import numpy as np

arr_s = np.arange(12).reshape(3,4)

print(arr_s)


# In[2]:


#convert to 1d list

arr_s.ravel()


# In[3]:


print(arr_s)


# Why hasn't our array changed? `reshape` returns a new array, `resize` changes the array ***in place***

# In[4]:


arr = np.arange(8)
arr_r = arr.reshape(4,2)

print(arr)
print(arr_r)


# In[5]:


arr.resize(4,2)
print(arr)


# # Special Arrays

# In[6]:


arr_0 = np.zeros((3,5)) #Why I have double paranthesis here?
print(arr_0)


# In[7]:


arr_0= np.zeros((2,2),dtype=bool)
arr_0


# In[8]:


arr_1= np.ones((2,3),dtype=int)
print(arr_1)


# In[9]:


from numpy.random import *
rand(4,3)

import numpy as np

np.random.rand(4,3)


# In[10]:


from numpy.random import *

int_from = -1
int_to = 17
randint(-1, 17, (4,3))

