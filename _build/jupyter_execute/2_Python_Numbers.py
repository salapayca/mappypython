#!/usr/bin/env python
# coding: utf-8

# # Numbers in Python

# Let's do some basic aritmethic operations with numbers:

# In[1]:


10+5


# Both 10 and 5 are integers and the result is an integer too!

# Next, we can do some division to see what happens our integers:

# In[2]:


10/4


# It is a float! Now, what can we do to get an integer? - floor division (//) 

# In[3]:


10//4


# With floor division we will get a truncated result. Now, try what happens if one of the numbers is negative:

# In[4]:


-10//4


# What if one the numbers is float?

# In[5]:


10.0//4


# No matter you are doing a floor division or not, if you have a float, you will get a float as a result.

# Common Operators for integers and floats in Python
# 
# |Operator|Description|Integer|Result|Floating Point|Result|
# | ------ | --------- | ----- |------|--------------|------|
# |-|Subtraction|9-2|?|9-2.0|?|
# |+|Addition|9+2|?|9+2.0|7|
# |/|Division|9/2|4.5|9/2.0|4.5|
# |//|Floor Division|9//2|4|9//2.0|4.0|
# |%|Modulus|9%2|?|9%2.0|?|
# |* |Multiplication|9 * 2|?|9* 2.0|?|
# |** |Exponent|9 ** 2|?|9** 2.0|?|
# 

# In[6]:


9%2.0


# Now, go ahead and try the all the operators to see what results you will get:

# <a href="3_Boolean_Logic.ipynb"> It is time for Boolean Logic!
