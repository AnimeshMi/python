#!/usr/bin/env python
# coding: utf-8

# # Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# In[12]:


def str(s):      
    u = sum(1 for i in s if i.isupper()) #using list comprehension for upper case
    l = sum(1 for i in s if i.islower())  #using list comprehension for lower case
    print( "No. of Upper case characters : %s,\n No. of Lower case characters : %s" %(u,l))

str("The quick Brow Fox")


# In[ ]:




