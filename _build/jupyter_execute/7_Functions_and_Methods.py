#!/usr/bin/env python
# coding: utf-8

# # Functions and Methods

# ## Working with Strings

# Many geoprocessing parameters are strings such as the names of workspace, the name of a feature class or the name of a field in a table. 
# Let's review some useful functions and methods which will help us to work with strings.

# The lower() method returns a lowercase version of the string value:

# In[1]:


mytext= "I AM LeaRNING GIS PRogRAmming"
print(mytext.lower())


# The upper() method returns a uppercase version of the string value:

# In[2]:


mytext = " I am learning GIS Programming"
print(mytext.upper())


# The title() method returns a title-case version of the string value:

# In[3]:


mytext = " I am learning GIS Programming"
print(mytext.title())


# The find()method identifies a substring and returns the lefmost index number when the string is found. A value of -1 is returned when the string is not found. Method is case sensitive. What would you expect as a result of below script?

# In[4]:


mystring = "Geographic Information Systems"
mystring.find("Info")


# The join() method is used to join elements of a list:

# In[5]:


list_gis = ["Geographic","Information","Systems"]
string_gis = " "
string_gis.join(list_gis)


# Here, the elements in the list are joined into a single string. The string object (string_gis) has a method called join(). The value of the string object, in this case, is a space (" "), and the argument of the join() method is the list of elements to be joined into a single string.

# The opposite of the join() is split(). Let's try to split our sentence:

# In[6]:


mystring = "I enjoy GIS Programming"
mylist = mystring.split(" ") #notice we used space hear but it could be anything. You can split from anywhere you like
print(mylist)


# Strip is usually used to manipulate path and file names. It allows you to remove any combination of characters in any order from the ends of an existing string. lstrip() and rstrip() gives a bit more control by limiting the direction. For example:

# In[7]:


mypath = "Commenting scripts is good"
print (mypath.rstrip("Cdo"))
print (mypath.lstrip("Cdo"))


# Calling one of the strip methods without any arguments removes leading or trailing spaces, also referred to as whitespace in coding. This method is useful for cleaning up strings that may have been formatted in another program. 

# In[8]:


myfile = "   I am reading my ASCII file here"
myfile.strip()


# ## The Power of Replace

# As the name implies, replace() method used to replace a substring with another substring. For example:

# In[9]:


mytopic = "GIS Scripting"
mytopic.replace("Scripting","Programming")


# ## DA PRINT

# You are going to use print function a lot! Either for checking your script is funcioning or not, or to let the end user about the final result. Now, let's see some examples of how we can use print function.  You can use __+__ sign before and/or after your variable depending on where it will be printed. If it is not a string, you have to use __str()__ to convert it to string first.

# In[10]:


#Casting
year =2020
print ( " It was hard to predict the spatial spread of the CoViD-19 pandemic in year "+str(year))


# Another way to concatenate your string is to use {} - curly brackets. They will look your print statement more elegant:

# In[11]:


year =2020
print ( "It was hard to predict the spatial spread of the CoViD-19 pandemic in year {0}".format(year))


# Here, {0} is replacement field. Can you guess why we have 0 in bracket? What if we have more than one variable to replace?

# In[12]:


studentname = "Seda"
studentnumber = 12345
print("{0}'s student number is {1}".format(studentname,studentnumber))


# Another approach is using % operator as a placeholder. For strings % is followed by s, other options are %i for integer, %d for decimal numbers.

# In[13]:


studentname = "Seda"
studentnumber = 12345
print("%s's student number is %i" %(studentname,studentnumber))


# And last, but not least, we have string literals where the expressions are replaced with their values at runtime. Let's see the example below:

# In[14]:


studentname = "Seda"
studentnumber = "12345"
print(f"{studentname}'s student number is {studentnumber}") # HAVE YOU NOTICED THE f 

