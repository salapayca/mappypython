#!/usr/bin/env python
# coding: utf-8

# # Block and Indendation in Python
# 
# ![indentation](Picture2.png)

# In[1]:


height = 1

if height > 6:
    print ("You are too tall!")


# ## Conditional Statements if-else
# 
# `if <condition>:
#     <statement>`
#     
# The `if` keyword is followed by a condition and then a **colon**. 
# Then there is a block of code—that is, one or more lines indented in the same manner. 
# - If the condition evaluates to **True**, the lines of code that make up the block are run. 
# - If the condition evaluates to **False**, the lines of code are skipped, and the program moves on to the next statement after the if structure. 
# 
# *So how does Python know when you have reached the end of the if structure? *
# 

# Let's start with basics: 

# In[2]:


x=0
if x < 0:
    print ("x is negative")
elif x == 0:
    print ("x is zero")
else:
    print ("x is positive")


# Remember your Lab 2 data? How about having a simple version? Let's find the maximum of this list. Hint : you can use `max()` function.

# In[3]:


terrain = [9,1,2,14]

max(terrain)


# That was easy. How about practicing if-else and finding the maximum. How should we get the maximum of the list? But before that let's understand how machines can find the maximum in a binary operation. 
# 
# ![findingmax](findingmax.png)

# In[4]:


maximum = 0


# In[5]:


terrain = [9,16,2,14]

maximum = 0

if terrain[0]>maximum:
    print ("New maximum is : ", terrain[0])
    maximum=terrain[0]
if terrain[1]>maximum:
    print ("New maximum is : ", terrain[1])
    maximum=terrain[1]
if terrain[2]>maximum:
    print ("New maximum is : ", terrain[2])
    maximum=terrain[2]
if terrain[3]>maximum:
    print ("New maximum is : ", terrain[3])
    maximum=terrain[3]


print(maximum)


# What should I fix below?

# In[6]:


maximum=0
terrain = [9,16,2,14]

for i in range(0, len(terrain)):
    if terrain [i]>maximum:
        print ("New maximum is : ", terrain[i])
        maximum=terrain[i]

print(maximum)


# In[7]:


maximum=0
for i in range(0, len(terrain)):
    if terrain [i]>maximum:
        print ("New maximum is : ", terrain[i])
        maximum=terrain[i]
        


# can you find the maximum of this?

# In[8]:


terrain = [[9,10],[2,4]]

max(terrain)


# In[9]:


terrain = [[9,10],[2,4]]


for i in range(0, len(terrain)):
  
    print(max(terrain[i]))
  


# In[10]:


terrain = [[9,10,13,8],[2,0,4,4],[5,9,1,4]]

maximum=0
n_rows= len(terrain)
n_cols=len(terrain[0])


for row in range(0,n_rows):
    for col in range(0,n_cols):
        if terrain[row][col]<maximum:
            maximum=terrain[row][col]
        
print(maximum)     


# In[11]:


for row in range(0, len(terrain)):
    for col in range(0, len(terrain[0])):
        #print(terrain[row][col])
        if terrain [row][col]>maximum:
         #   print ("New maximum is : ", terrain[row][col])
            maximum=terrain[row][col]
print(maximum)

