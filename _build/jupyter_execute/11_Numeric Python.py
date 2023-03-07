#!/usr/bin/env python
# coding: utf-8

# # Numeric Python - NumPy
# 
# - Third party module for fast management of multidimensional grid-like data
# - [Source](http://numpy.scipy.org/)
# - Documentation
#     - [Numpy Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
#     - [Numpy Examples](https://scipy.github.io/old-wiki/pages/Numpy_Example_List_With_Doc.html)

# # ARRAY
# 
# - Basic data structure of numerical python : **array**
# - Arrays are multi dimensional lists of homogenous data (i.e. no mixing of data types are allowed)
#     e.g. 2 dimensional integer array is equivalent to a list of lists of integers
# - More efficient than standard Python data types for very large sets of numbers (large grids)
# - All numbers in an array are of the same data type
# 

# - Array objects must be full (no empty cells) 
# - `ndim` - the number of dimensions alogn which that array is defined
# - `size` - total number of elements in array
# - `shape` - the number of dimensions an array has and the extent of each of these dimensions
# 

# ## Examples

# In[7]:


list2d = [[1.0,2.0,3.0,4.0],[4.0,3.0,2.0,1.0]]

print(list2d)
type(list2d)


# In[8]:


import numpy 

arr = numpy.array(list2d)

print(arr)
type(arr)


# In[3]:


arr.ndim # dimensions(number of axes)


# In[4]:


arr.shape # shape ( number of rows,cols)


# In[5]:


arr.size #total number of elements


# In[9]:


arr.dtype #array data type


# ## Example : Creating A Boolean Array

# In[10]:


import numpy as np
arr_b = np.array([[1,1,0],[0,1,0]], dtype=bool)

print(arr_b)


# In[11]:


#how much memory?
arr.itemsize


# In[17]:


# A common error in array building:
arr_e = np.array([1,2]
print(arr_e)


# In[13]:


arr_e = np.array([1,2,3,4,5])
print(arr_e)


# In[14]:


#Create an array from a range of values
arr_r = np.arange(0.0, 3.0,0.5) # note that you can use a fraction as a step
print(arr_r)

