#!/usr/bin/env python
# coding: utf-8

# # Working with Lists
# 
#  There are couple of nice built-in functions which will be handy while we are doing our geoprocessing analysis. The first one is len() function, which returns the number of items in a list.

# In[1]:


new_england_states = ["Rhode Island", "Massachusetts", "New Hampshire",                       "Maine", "Vermont", "Connecticut"]
len(new_england_states)


# We can sort() our list : if it consists of words, it will be alphanumetical, it if it consists of numbers, it will be from smallest to largest. If you would like to reverse the order, you can use reverse():

# In[2]:


new_england_states.sort()
print(new_england_states)
new_england_states.reverse()
print(new_england_states)


# Python is a zero-indexed language and list items are indexed starting from zero. You can obtain any list item by using this index number.

# In[3]:


print(new_england_states)
new_england_states[2]


# You can use negative index numbers to start counting from the end. The last item in the list will be returned with an index number -1.

# In[4]:


new_england_states[-1]


# Lists can be sliced into smaller lists. Slicing uses two indices separated by a colon. The first index is the number of the first element you want to include. The second index is the number of the first element you dont want to include. If you don't provide any number, it will start from the very beginning or the end (depending on which one you are leaving out). Let's see in examples:

# In[5]:


print (new_england_states)
print (new_england_states[0:3])
#print (new_england_states [2:])
#print (new_england_states [:-2])


# Notice that if we call an item from a list by using the corresponding index number, it will be obtained as a string. However, if we would like to obtain as a list, we need to use the code below:

# In[6]:


mass_string = new_england_states[3] #string
mass_list = new_england_states[3:4] # list

print(type(mass_string))
print(mass_string)

print(type(mass_list))
print(mass_list)


# In[7]:


my_numbers = [1,2,3,4]
print(my_numbers[0])
print(my_numbers[0:1])


# You can delete the items from a list by using del statement based on the index number:

# In[8]:


del new_england_states[-1]
print(new_england_states)


# ## Creating an Empty List

# You can also create an empty list and then add elements to it. This will be quite helpful if you are obtaining the elements from a function or from another source. 

# In[9]:


mylist = []
print(mylist)
mylist.append("Counties")
print(mylist)


# You can also create list of characters from a string as follows:

# In[10]:


mypath = "https://twitter.com/GisProgramming"
letter_mypath = list(mypath)
print (letter_mypath)


# Note that this does not work for number since they are not iterable, if you would like to conver a number to list, you must first conver the value to an iterable first.
# ![A_picture_describes_iterables](Iterables-and-iterators.jpg)

# In[11]:


fibonacci_numbers = 112358
list(str(fibonacci_numbers))


# If you would like to add the number as it is, then you can create an empty list and then add the number by using append().

# ## Commonly Used List Methods

# Now, let's look at other commonly used list methods such as append(), count(), extend(), index(), insert(), pop(), and remove().
# Check all the available methods of list objects from <a href="https://docs.python.org/3/tutorial/datastructures.html">here</a>.

# ### list.append(x)
# The append() method appends an element to the end of the list

# In[12]:


cities = ["Amherst", "Boston"]
cities.append("Newton")
print (cities)


# ### list.count(x)
# The count() method determines the number of the times an element occurs in a list:

# In[13]:


numbers = [1,2,3,2,2,2,2,4,4,1,1,1,1]
numbers.count(1)


# ### list.extend(iterable)
# The extend() method allows you to append several values at once:

# In[14]:


list1 = [1,2,3,4]
list2 = [5,6,7,8,9,10]

list1.extend(list2)
print (list1)


# ### list.index(i)
# The index() method finds the index of the first occurance of a value:

# In[15]:


new_england_states = ["Rhode Island", "Massachusetts", "New Hampshire", "Maine", "Vermont", "Connecticut"]
new_england_states.index("Maine")


# ### insert()
# The insert() method makes it possible to insert an element into a list at a specified location.

# In[16]:


new_england_states = ["Rhode Island", "Massachusetts", "New Hampshire", "Maine", "Vermont"]
new_england_states.insert(1,"Connecticut")
print (new_england_states)


# ### list.pop()
# The pop() removes an element from a list and returns it.

# In[17]:


new_england_states = ["Rhode Island", "Massachusetts", "Rhode Island","New Hampshire", "Maine", "Vermont"]
new_england_states.pop(0)


# ### list.remove(x) 
# The remove() method removes the first occurance of a value, as follows:

# In[18]:


numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
numbers.remove(3)


# ### range(start, stop, step)

# In[19]:


a = range(6)
b = range(2,6)
c = range(1,10,5)

print(a)
print(b)
print(c)

for item in c:
    print (item)


# ### len(object)

# In[20]:


len(numbers)


# ## String Lists

# Strings are the stored as list, and therefore have an index positioning system starting from 0 because Python is a zero-based language. Each character is assigned to an index number. 

# In[21]:


mystring = "GIS Programming"
mystring[0]


# You can obtain any character by changing the index value - you are welcome to try by yourself!

# You can use negative index numbers to start counting from the end. The last item in the list will be returned with an index number -1.

# In[22]:


mystring[-2]


# How about obtaining a slice from our string? You can specify the starting and ending index numbers and you will get the slice that you are interested in :

# In[23]:


mystring[0:3] #notice that the second index valued character is not included - it tells python to where to stop!


# OK, what if you are intested in something from the beginning to a point that you are intested in, or the from a starting point until the end. Let's see how we can achieve that:

# In[24]:


mypath = "https://twitter.com/GisProgramming"
print(mypath[8:])
print(mypath[:-14])


# If you have a long string or even a file and you don't want to sit and count every single character, you can simply use find() which will return the index number that you are looking for:

# In[25]:


mypath.find("Gis") # if you are not paying attention to the upper or lower case,
                   # or there is no value equals to what you are searching for then it will return -1


# The join() will help you to join elements of a list:

# In[26]:


mypath = ["https://", "twitter.com","/","GisProgramming"]
myfullpath =""
myfullpath.join(mypath)


#     
# <a href="6_List_of_Lists.ipynb">Let's move to the next section to learn more!</a>
# 

# In[ ]:




