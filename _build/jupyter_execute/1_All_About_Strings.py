#!/usr/bin/env python
# coding: utf-8

# # Algebra of Strings

# Algebra? Strings? It sounds oxymoron, right? Afterall, strings are nothing but characters so how come we do addition, multiplication, substraction or division on them? 
# While using python scripting in our spatial analysis, we will be using a lot of unicode characters. Strings can be any characters (letters, numbers, symbols, and what not) but python will know that they are string when we use ```" "``` quotaton marks. 

# ## Addition 
# 
# In the below example, we will see how we can combine several strings and print the output. 
# You can joining two strings using ```addition(+)``` operation

# In[2]:


a = "I"
d= " "
b = "love"
c = "GIS"
print(a+d+b+d+c)


# Notice how the variable ```d``` is holding only empty space as a value. The string addition is referred as **string concatenation**. It might be very useful when you need to add file names to file paths.

# Strings can contain numeric characters as well. However, we should be careful to convert any number to integer before combining them:

# In[3]:


temp = "30"
print ( "The temperature is " +temp+ " Celcius degrees today!")


# OK, let's use str() then

# In[4]:


temp = 30
print ("The temperature is " + str(temp)+ " Celcius degrees today!")
print ("And yes, I like Celcius better than Fahrenheit!")


# UTF-8 contains 1.1 million different character codes that enable us to any character we want in our prints! Hmm, why not to try to write my surname properly then:)

# In[5]:


print ("Hello! My name is Seda \u015ealap Ay\u00e7a")
print("\u015e is read as sh sound")
print("\u00e7 is read as ch sound")

#source : http://sercanulucan.com/archive/unicode-utf8/


# ## Multiplication

# Addition is not the algebric operation that works on strings. You can also use ```multiplication```! The below code enables you to print a string multiple times:

# In[1]:


n= int(input("How many times you need to repeat:"))
my_string = "Python\n"
print(my_string*n)


# (stringlist)=
# ## Subtraction
# 
# Strings are the stored as list, and therefore have an index positioning system starting from 0 because Python is a zero-based language. Each character is assigned to an index number. 
# 

# In[3]:


mystring = "GIS Programming"
mystring[0]


# You can obtain any character by changing the index value - you are welcome to try by yourself.You can use negative index numbers to start counting from the end. The last item in the list will be returned with an index number -1.

# In[4]:


mystring[-2]


# How about obtaining a slice from our string? You can specify the starting and ending index numbers and you will get the slice that you are interested in :

# In[6]:


mystring[0:3] #notice that the second index valued character is not included - it tells python to where to stop!


# OK, what if you are intested in something from the beginning to a point that you are intested in, or the from a starting point until the end. Let's see how we can achieve that:

# In[7]:


mypath = "https://twitter.com/GisProgramming"
print(mypath[8:])
print(mypath[:-14])


# If you have a long string or even a file and you don't want to sit and count every single character, you can simply use ```find()``` which will return the index number that you are looking for:

# In[8]:


mypath.find("Gis") # if you are not paying attention to the upper or lower case,
                   # or there is no value equals to what you are searching for then it will return -1


# The ```join()``` will help you to join elements of a list:

# In[9]:


mypath = ["https://", "twitter.com","/","GisProgramming"]
myfullpath =""
myfullpath.join(mypath)


# ## Division
# We don't have divide for strings, but we can split them! Let's use ```split``` function in action:

# In[10]:


my_string = "This is a string in Python"
my_list = my_string.split(' ')
print(my_list)

