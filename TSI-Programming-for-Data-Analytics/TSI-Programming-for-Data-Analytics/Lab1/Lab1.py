#!/usr/bin/env python
# coding: utf-8

# # Exercises (homework)
# 
# Please organise your solutions as a separate notebook and upload to the LMS (Moodle):
# * Notebook (.ipynb)
# * Generate pdf (File -> Download as -> PDF).
# 
# Pandoc is required and can be installed as
# 
# _conda install -c conda-forge pandoc_
# 
# in Anaconda prompt

# ### Exercise 1.
# Calculate sum and product of two integer numbers:

# In[10]:


number1 = 5

number2 = 7

#YOUR CODE HERE

print(f"Sum of {number1} and {number2} is {number1 + number2}; product of {number1} and {number2} is {number1 * number2}")

# Expected result: "Sum of 5 and 7 is 12; product of 5 and 7 is 35" printed


# ### Exercise 2.
# Repeat the string n times (Hint: check the ** operator for strings)

# In[2]:


times = 5
s = "Hey! "

# YOUR CODE HERE

print(s * times)

# Expected result: "Hey! Hey! Hey! Hey! Hey! " printed


# ### Exercise 3.
# Calculate the age given the year of birth

# In[3]:


birth_year = 1980

# YOUR CODE HERE

import datetime

datetime.date.today()
current_year = datetime.date.today().year

x = current_year - birth_year -3
y = current_year - birth_year -2
print(f"Your age is {x} or {y} years")

# Expected result: "Your age is 41 or 42 years"


# ### Exercise 4.
# Divide two integers with a remainder

# In[4]:


dividend = 17
divisor = 6

# YOUR CODE HERE

x = (dividend / divisor)
y = divisor
n = str(x)

print("The quotient is",n[0] , "and the remainder is" ,n[-1] ,)

# Expected result: "The quotient is 2 and the remainder is 5"


# ### Exercise 5.
# Print pi (math.pi) with 10 decimal places

# In[5]:


import math

# YOUR CODE HERE

math.pi
Pi = math.pi

print("Pi is", round(Pi,10))

# Expected result: "Pi is 3.1415926536"


# ### Exercise 6.
# Introduce variables with current exchange rates and convert 10 euro to pounds (GBP) and dollars ($)

# In[6]:


value = 10 # euro

# YOUR CODE HERE

gbp = 0.862650
usd = 1.060400
GBP = value * gbp
USD = value * usd

print("10 euro is", round(GBP,2), "pounds (GBP) or", round(USD,2),"dollars (USD)")

# Expected result (approx.): "10 euro is 8.68 pounds (GBP) or 10.02 dollars (USD)


# ### Exercise 7.
# Print a string by one symbol in line

# In[7]:


name = "Sergejs" # repalce with your name

# YOUR CODE HERE

for name in "Sergejs":
    print(name)
    
# Expected result:
# D
# m
# i
# t
# r
# y


# ### Exercise 8.
# Calculate the age given the date of birth

# In[8]:


birth_date = "1980-Jul-6"
birth_date = "1980-Jul-6"

# YOUR CODE HERE

from datetime import datetime

str_birth_date = datetime.strptime(birth_date, "%Y-%b-%d").year
str1 = str_birth_date

import datetime
datetime.date.today()
dt = datetime.date.today().year
today = dt - str1 -2

print("Your age is", today, "years")

# Expected result: "Your age is 42 years"

