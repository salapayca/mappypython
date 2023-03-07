#!/usr/bin/env python
# coding: utf-8

# # Looping Syntax 
# 
# Loops are used for repetitive tasks:
# 
# Instead of this:
# 
# `print("string")
#  print("string")
#  print("string")
#  print("string")`
# ...
# 
# You can do this:
# 
# `x=1
#  while x<5:
#     print("string")`

# In[1]:


x=1
while x<5:
    print("string")
    print("Current x  is :",x)
    x=x+1
    print("Final x  is :",x)


# ## Counted Loop
# 
# `for x in range(1,5):
#     print (x)`

# In[2]:


for x in range(1,5):
    print(x)


# In[3]:


# counted loop
n = range(1,10,5)
print(n)
for i in n:
    print (i, "python")


# ## List Loop
# 
# - Lost loops iterate over the value in a list
# - The loop will execute once for each value in the list

# In[4]:


# list loop
mylist = [[1,2],[3,6],[4,5]]
# number of columns in a multi dimensional list - len(mylist[0]) ->2
# number of rows len(mylist) ->3
for item in mylist:   
    print (item, "times Python")
   


# In[5]:


# breaking out of loops
# find the maximum number below 1000 that divides by 12
for n in range(1000, 0, -1):
    print(n)
    div = n % 12
    print(div)
    if div == 0:
        print (n)
        break



# Q1)Why use break above?

# In[6]:


cv = [[0.1,1],[0.5,11],[0.8,3]]
cw=0.6

#calculate overall score list for single criterion

dlist = []
for i in cv:
    dlist = dlist +i
    print(dlist)
    
   # overall = i*cw
   #print(overall)
    
overalls=[]
for i in dlist:
    overall= i*cw
    overalls.append(overall)
    
print(overalls)    
#for i in range(0, len(cv)):
#    print(i)


# In[7]:


cv = [0.1,0.5,0.8]
cw=0.6

overall =[]

for i in range(0, len(cv)):
    overall.append(cv[i]*cw)
    
print (overall)


# In[8]:


cv1= [0.1,0.5,0.8]
cv2 = [0.2,0.3,0.4]
cw=[0.6, 0.4]
overalls=[]



#check if the both criterion has the equal number of elements
#calculate overall score list for criteria


# In[9]:


cv1= [0.1,0.5,0.8]
cv2 = [0.2,0.3,0.4]
cw=[0.6, 0.4]
overalls=[]

cw[1]

if len(cv1)==len(cv2):
    for i in range(0,len(cv1)):                
        overall = cv1[i]*0.6+cv2[i]*0.4
        
        overalls.append(overall)
    print(overalls)
else:
    print("Criteria lists are not equal!")

