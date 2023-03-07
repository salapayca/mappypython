#!/usr/bin/env python
# coding: utf-8

# # Algebra of Strings

# While using python scripting in our spatial analysis, we will be using a lot of unicode characters. Strings can be any characters (letters, numbers, symbols, and what not) but python will know that they are string when we use ```" "``` quotaton marks. In the below example, we will see how we can combine several strings and print the output. 
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


# Addition is not the algebric operation that works on strings. You can also use ```multiplication```! The below code enables you to print a string multiple times:

# In[4]:


n= int(input("How many times you need to repeat:"))
my_string = "Python\n"
print(my_string*n)


# We don't have divide for strings, but we can split them! Let's use ```split``` function in action:

# In[5]:


my_string = "This is a string in Python"
my_list = my_string.split(' ')
print(my_list)

