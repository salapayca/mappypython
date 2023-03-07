#!/usr/bin/env python
# coding: utf-8

# ## Multi-dimensional Lists
# 
# We can store lists within lists.
# 
# 
# ![list_of_lists](listoflist-768x432.jpg)
# 
# Picture Source : https://blog.finxter.com/python-list-of-lists/

# In[1]:


mylist= [[1,2],[3,4],[5,6]]

print(mylist)


# The inner list can hold the coordinates, criteria value-weight pair, or anything that you can think of! 

# Let's assume that we are given three polygons' criteria values and weights as a pair list : where the first element is criteria value and the second one is criteria weight [v,w]. 
# 
# And we want to make sure the criteria weights' sum is 1. Let's do a step by step calculation and see how we can achieve this task successfully.

# In[2]:


pairs =[[0.3,0.12],[0.4,0.6],[0.7,0.38]]
pairs


# Q1)First let's check how we can get the first pair from our pairs list:

# In[3]:


pairs[0]


# Q2)Good job! Now, let's try how we can get only the weight of first polygon:

# In[8]:


cw= pairs[0][3]
print(cw)


# We are going to learn about loops and how to iterate through list soon but before that let's assume we would like to do a basic sum operation for each weight. Create one variable per weight and sum them to see if they are equal to 1 or not. You can check this by using a Boolean operation.

# In[ ]:


cw1=pairs[0][1]
cw2=pairs[1][1]
cw3=pairs[2][1]

total =cw1+cw2+cw3

total==1


#     
# <a href="7_Functions_and_Methods.ipynb">Let's move to the next section to learn more!</a>
# 
# 
