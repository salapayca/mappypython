#!/usr/bin/env python
# coding: utf-8

# ## Boolean Operators

# Boolean operators evaluate whether a variable or expression is True or False. These Boolean values are case sensitive so true or TRUE will produce an error. We can compare two Booleans by using and or or operators. The or operator results in True if either Boolean is True.

# In[1]:


a = True
b = False
a or b


# The and operator results in True only if both Booleans are True:

# In[2]:


a and b


# What happens if we have empty string variable or zero? Let's check and see if they are True or False:

# In[3]:


text = "I am telling the truth"
number = 1
print(bool(text))
print(bool(number))


# In[4]:


notext =""
zero = 0
print(bool(notext))
print(bool(zero))


# Any number other than 0 and 0.0 is always True.

# We can test the equivalance of two expression by using **is** keyword, too. The difference between == and is , equal to compares the values of the variables, not the objects themselves.

# In[5]:


list1 = [1,2,3]
list2 = [1,2,3]
list1 is list2


# In[6]:


list1 = [1,2,3]
list2 = [1,2,3]
list1 == list2


# <a href="4_Order_of_Operations.ipynb"> Next topic : Order of Operations
