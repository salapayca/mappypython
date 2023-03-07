#!/usr/bin/env python
# coding: utf-8

# ## HANDS-ON TIME 
# 
# 

# 1. Practice while loop with else from [Programiz.com](https://www.programiz.com/python-programming/while-loop). You can use the empty code cell below to test your codes.

# In[1]:


#while loop with else

counter = 0

while counter<3 :
    print ("Inside loop")
    counter = counter +1
    print(counter)
else:
    print ("Inside else")


# <center><img src="https://i.etsystatic.com/6854467/r/il/87fa53/1383013322/il_570xN.1383013322_31ab.jpg" width=300 height=300 align="center"/></center>

# 2. Imagine you are in a _Python_ restaurant which serves menu as a list. And, you are a hungry caterpillar who wants to eat everything! And frankly, you can order your food by print statements. Write a for loop to print the names of the foods that you want to eat. 

# In[2]:


menu_pycafe = ["one ice-cream cone", "one pickle", "one slice of Swiss cheese", "one slice of salami",
               "one lollipop", "one piece of cherry pie", "one sausage", "one cupcake and one slice of watermelon"]
#your code goes here

for i in menu_pycafe:
    print ("I would like " +i)
len(menu_pycafe)


# <center><img src="https://static1.squarespace.com/static/5c62c09c4d546e27dc1016c7/5c71f65a9140b72b900c47e2/5c846bca24a694a6a027ee65/1552182810224/BTTF+In+Concert.jpg?format=500w" width=300 height=300/></center>

# 3. You have a time machine which will take you from 2020 to 2050, and you would like to write a count-down script so that you will know which year you are in! Use a while loop to count down and don't forget to print each year that you pass, Marty! 

# In[3]:


year_traveled = 2020
print("Starting Year:"+str(year_traveled))
while year_traveled<2050:
    print ("Travel to the Future ->")
    year_traveled = year_traveled +1
    print("Year:"+str(year_traveled))
else:
    print ("Congrats! You arrived at the Future!")
    print("Year:"+str(year_traveled))


# In[4]:


years = list(range(2050, 2020,-1))

for i in years:
    while i > 2019:
        print(i)
        i = i-1

